#!/usr/bin/env python3

from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os
import getpass

URL = 'https://ihk-bic-online.de/tibrosBB/BB_pruefer.jsp'
URL_PRUEFER = 'https://ihk-bic-online.de/tibrosBB/projektePrueferAnsicht.jsp'

TIBROS_USER = os.environ.get('TIBROS_USER', '') 
if TIBROS_USER == '':
    TIBROS_USER = input('Benutzername: ')    
TIBROS_PASS = os.environ.get('TIBROS_PASS', '') 
if TIBROS_PASS == '':
    TIBROS_PASS = getpass.getpass('Passwort: ')

print(f'ENV-VARS {TIBROS_USER=} TIBROS_PASS')

def element_by_name(f:Firefox, element_name):
    return f.find_element(By.NAME, element_name)

def login(f:Firefox):
    f.get(URL)
    element_by_name(f, 'login').send_keys(TIBROS_USER)
    element_by_name(f, 'pass').send_keys(TIBROS_PASS)
    element_by_name(f, 'anmelden').click()

def main():
    # https://selenium-python.readthedocs.io/faq.html?highlight=save#how-to-auto-save-files-using-custom-firefox-profile
    fp = FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")

    f = Firefox(fp)

    print('exportiere IHK-Anträge')
    
    login(f)
    if 'captchaGuard' in f.current_url:
        print('Löse das CAPTCHA, drücke danach enter zum Fortfahren')
        input()

    f.get(URL_PRUEFER)

    Select(element_by_name(f, 'ptermin')).select_by_index(1)
    element_by_name(f, 'search').click()
    element_by_name(f, 'download').click()

    f.close()

if __name__ == '__main__':
    main()
