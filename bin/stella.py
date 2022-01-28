#!/usr/bin/env python3

from logging.config import IDENTIFIER
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os

URL = 'https://www.schulministerium.nrw.de/BiPo/Stella/online'
ORT = os.environ.get('ORT', 'Bochum')
UMKREIS = os.environ.get('UMKREIS', 20) # km

print(f'Suche nach Stellen in Stella')
print(f'{ORT=} {UMKREIS=} \n{URL=}')

f = Firefox()
f.get(URL)
f.find_element(By.LINK_TEXT, 'zu den Stellen').click()
f.find_element(By.LINK_TEXT, 'Sonstige Stellen').click()
inst = Select(f.find_element(By.ID, 'institution'))
inst.select_by_visible_text('Sonstiges')
ort = Select(f.find_element(By.ID, 'ort'))
ort.select_by_visible_text(ORT)

inp = f.find_element(By.ID, 'umkreis')
inp.clear()
inp.send_keys(str(UMKREIS))

f.find_element(By.NAME, 'button_suchen').click()
f.find_element(By.LINK_TEXT, '500').click()

rows = f.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
for row in rows:
    cell = row.find_element(By.TAG_NAME, 'td').text
    # remove double white spaces
    cell = " ".join(cell.strip().split())
    print('- ', cell)

f.close()
