#!/usr/bin/env python3

import time
import os
import getpass
import datetime
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

URL = 'https://cissa.webuntis.com/WebUntis/?school=bk-bochum#/basic/login'
URL_ABSENCE = 'https://cissa.webuntis.com/absence-times'

KLASSEN = os.environ.get('KLASSEN', 'ITF19a,ITF20a,ITF21a')
DAYS_BACK = os.environ.get('DAYS_BACK', 30)
FINISH_WAIT_SECONDS = os.environ.get('FINISH_WAIT_SECONDS', 3)
UNTIS_USER = os.environ.get('UNTIS_USER', 'bak')
UNTIS_PASS = os.environ.get('UNTIS_PASS', '')
if UNTIS_PASS == '': 
    UNTIS_PASS = getpass.getpass()

print(f'ENV_VARS: {UNTIS_USER=} {KLASSEN=} {DAYS_BACK=} {FINISH_WAIT_SECONDS=}')
KLASSEN = KLASSEN.split(',')

f = Firefox()

def login(f:Firefox):
    f.get(URL)
    for lbl in f.find_elements(By.TAG_NAME, 'label'):
        if lbl.text == 'Benutzername':
            f.find_element(By.ID, lbl.get_attribute('for')).send_keys(UNTIS_USER)
        if lbl.text == 'Passwort':
            f.find_element(By.ID, lbl.get_attribute('for')).send_keys(UNTIS_PASS)

    for btn in f.find_elements(By.TAG_NAME, 'button'):
        if btn.text == 'Login':
            btn.click()

def select(f:Firefox, id_name, selection_text):
    Select(f.find_element(By.ID, id_name)).select_by_visible_text(selection_text)

def process_klasse(klasse):    
    print(f'# Fehlzeiten {klasse}')
    select(f, 'klasseOrStudentgroupId', klasse)

    time.sleep(FINISH_WAIT_SECONDS)
    try:
        tab = f.find_element(By.ID, 'absenceTimesForm.absences')
    except NoSuchElementException:
        print(f'Keine Einträge für {klasse}')
        return

    # traverse table
    tab_header = tab.find_elements(By.TAG_NAME, 'th')
    tab_header = [h.text for h in tab_header]
    idx_name = tab_header.index('Schüler*innen')
    idx_date = tab_header.index('Datum')
    idx_days = tab_header.index('Fehltage')
    idx_txt = tab_header.index('Text')
    tab_body = tab.find_element(By.TAG_NAME, 'tbody')
    for row in tab_body.find_elements(By.TAG_NAME, 'tr'):
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells[idx_days].text != '0':
            print(cells[idx_name].text, cells[idx_date].text, cells[idx_txt].text)

login(f)
f.get(URL_ABSENCE)
# wait some seconds for page to load
time.sleep(FINISH_WAIT_SECONDS)
# navigate to iframe
iframes = f.find_elements(By.TAG_NAME, 'iframe')
f.switch_to.frame(iframes[0])

select(f, 'excuseStatusId', 'nicht entsch.')

# set start date
start_day = datetime.date.today() - datetime.timedelta(days=DAYS_BACK)
start_day = start_day.strftime('%d.%m.%Y')
start_date = f.find_element(By.ID, 'absenceTimesForm.idstartDate')
start_date.clear()
start_date.send_keys(start_day)
start_date.send_keys(Keys.TAB)

for klasse in KLASSEN:
    process_klasse(klasse)

#f.switch_to_default_content()
if input('close? y/n ') == 'y':
    f.close()
