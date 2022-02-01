#!/usr/bin/env python3

import os
import getpass
import datetime
import click
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

SCHOOLID = os.environ.get('SCHOOLID', 'bk-bochum')
URL = f'https://cissa.webuntis.com/WebUntis/?school={SCHOOLID}#/basic/login'
URL_ABSENCE = 'https://cissa.webuntis.com/absence-times'

FINISH_WAIT_SECONDS = int(os.environ.get('FINISH_WAIT_SECONDS', 3))
UNTIS_USER = os.environ.get('UNTIS_USER', '')
if UNTIS_USER == '':
    UNTIS_USER = input('Untis user: ')
UNTIS_PASS = os.environ.get('UNTIS_PASS', '')
if UNTIS_PASS == '': 
    UNTIS_PASS = getpass.getpass("Untis-Passwort: ")


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
    sel = Select(f.find_element(By.ID, id_name))       
    for option in sel.options:
        if selection_text.lower() in option.text.lower():
            sel.select_by_visible_text(option.text)
            return

def process_klassen(f:Firefox):
    f.minimize_window()
    select(f, 'klasseOrStudentgroupId', '- Alle -')

    try:
        tab = f.find_element(By.ID, 'absenceTimesForm.absences')
    except NoSuchElementException:
        print(f'Keine Einträge')
        return

    # traverse table
    tab_header = tab.find_elements(By.TAG_NAME, 'th')
    tab_header = [h.text for h in tab_header]
    idx_name = tab_header.index('Schüler*innen')
    idx_klasse = tab_header.index('Klasse')
    idx_date = tab_header.index('Datum')
    idx_days = tab_header.index('Fehltage')
    idx_txt = tab_header.index('Text')
    tab_body = tab.find_element(By.TAG_NAME, 'tbody')
    for row in tab_body.find_elements(By.TAG_NAME, 'tr'):
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells[idx_days].text != '0':
            print(
                cells[idx_klasse].text, 
                cells[idx_name].text, 
                cells[idx_date].text, 
                cells[idx_txt].text)


@click.command()
@click.option('--name', default='', help='Beschränke Anzeige auf Schülernamen' )
@click.option('--days_back', default=30, 
    help='Anzahl betrachteter Tage in der Vergangenheit (default 30)')
def show(name, days_back):
    'Abwesenheiten listen'

    print(f'ENV_VARS: {SCHOOLID=} {UNTIS_USER=} {FINISH_WAIT_SECONDS=}')

    f = Firefox()
    f.implicitly_wait(FINISH_WAIT_SECONDS)

    login(f)
    f.get(URL_ABSENCE)
    # navigate to iframe
    iframes = f.find_elements(By.TAG_NAME, 'iframe')
    f.switch_to.frame(iframes[0])

    select(f, 'excuseStatusId', 'nicht entsch.')

    # set start date
    start_day = datetime.date.today() - datetime.timedelta(days=days_back)
    start_day = start_day.strftime('%d.%m.%Y')
    start_date = f.find_element(By.ID, 'absenceTimesForm.idstartDate')
    start_date.clear()
    start_date.send_keys(start_day)
    start_date.send_keys(Keys.TAB)

    # search for student
    if name != '':
        select(f, 'studentId', name)

    print(f'# Unentschuldigte Fehlzeiten der letzten {days_back} Tage')
    process_klassen(f)

    #f.switch_to_default_content()
    if input('close? y/n ') == 'y':
        f.close()

if __name__ == '__main__':
    show()
