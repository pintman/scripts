#!/usr/bin/env python3

import time
import os
import getpass
import datetime
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

URL = 'https://cissa.webuntis.com/WebUntis/?school=bk-bochum#/basic/login'
URL_ABSENCE = 'https://cissa.webuntis.com/absence-times'

KLASSE = os.environ.get('KLASSE', 'ITF19a')
DAYS_BACK = os.environ.get('DAYS_BACK', 30)
FINISH_WAIT_SECONDS = os.environ.get('FINISH_WAIT_SECONDS', 3)
USER = os.environ.get('USER', 'bak')
PASS = os.environ.get('PASS', '')
if PASS == '': 
    PASS = getpass.getpass()

print(f'{USER=}, {KLASSE=} {DAYS_BACK=} {FINISH_WAIT_SECONDS=}')

f = Firefox()

def login(f:Firefox):
    f.get(URL)
    for lbl in f.find_elements(By.TAG_NAME, 'label'):
        if lbl.text == 'Benutzername':
            f.find_element(By.ID, lbl.get_attribute('for')).send_keys(USER)
        if lbl.text == 'Passwort':
            f.find_element(By.ID, lbl.get_attribute('for')).send_keys(PASS)

    for btn in f.find_elements(By.TAG_NAME, 'button'):
        if btn.text == 'Login':
            btn.click()

def select(f:Firefox, id_name, selection_text):
    Select(f.find_element(By.ID, id_name)).select_by_visible_text(selection_text)

login(f)
f.get(URL_ABSENCE)
# wait some seconds for page to load
time.sleep(FINISH_WAIT_SECONDS)
# navigate to iframe
iframes = f.find_elements(By.TAG_NAME, 'iframe')
f.switch_to.frame(iframes[0])

select(f, 'klasseOrStudentgroupId', KLASSE)
select(f, 'excuseStatusId', 'nicht entsch.')

# set start date
start_day = datetime.date.today() - datetime.timedelta(days=DAYS_BACK)
start_day = start_day.strftime('%d.%m.%Y')
start_date = f.find_element(By.ID, 'absenceTimesForm.idstartDate')
start_date.clear()
start_date.send_keys(start_day)
start_date.send_keys(Keys.TAB)
start_date.click()

#f.switch_to_default_content()
#f.close()
