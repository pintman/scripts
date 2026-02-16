#!/usr/bin/env python3

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

URL = 'https://stadtbuecherei.bochum.de/opax/de/qsel.html.S'

def main():
    print(f'Brettspiele in der Bochumer Stadtbücherei')

    f = Firefox()
    f.set_page_load_timeout(30)

    # navigate to target page and start query
    f.get(URL)
    inp = f.find_element(By.NAME, 'FLD4')
    inp.send_keys('Spiel')
    inp.send_keys()
    # TODO add media type "Spiele"
    #f.find_element(By.NAME, 'MT').click()

    f.find_element(By.PARTIAL_LINK_TEXT, 'Anfrage starten').click()

    BLACKLIST_WORDS = ['Titel in den Medienkorb', 'Vormerkung']

    # navigate result rows
    continue_search = True
    while continue_search:
        table = f.find_element(By.CLASS_NAME, 'tab21')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            td = row.find_elements(By.CLASS_NAME, 'td01x09n')[0:3]
            if not td:
                continue
            cell = ' '.join([t.text for t in td])
            if cell == '' or cell in BLACKLIST_WORDS:
                continue

            print(cell)
            print('--')
        
        next_page = f.find_elements(By.LINK_TEXT, 'Nächste Seite')
        if next_page:
            next_page[0].click()
        else:
            continue_search = False
        
    f.close()

if __name__ == '__main__':
    main()
