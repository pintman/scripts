#!/usr/bin/env python3

import datetime

stunden_abend = [
    (datetime.time(15, 0), 9),
    (datetime.time(15, 45), 10),
    (datetime.time(16, 30),   'Pause'),
    (datetime.time(17, 0), 11),
    # Beginn Abendunterricht
    (datetime.time(17, 45), 12),
    (datetime.time(18, 30), 13),
    (datetime.time(19, 15),   'Pause'),
    (datetime.time(19, 30), 14),
    (datetime.time(20, 15), 15)
]

stunden_allgemein = [
    (datetime.time(7, 30), 1),
    (datetime.time(8, 15), 2),
    (datetime.time(9, 0),   'Pause'),
    (datetime.time(9, 15), 3),
    (datetime.time(10, 0), 4),
    (datetime.time(10, 45), 'Pause'),
    (datetime.time(11, 0), 5),
    (datetime.time(11, 45), 6),
    (datetime.time(12, 30), 'Pause'),
    (datetime.time(12, 45), 7),
    (datetime.time(13, 30), 8)
    ]
stunden_allgemein.extend(stunden_abend)

stunden_masch = [
    (datetime.time(9, 0), 1),
    (datetime.time(8, 45), 2),
    (datetime.time(9, 30),  'Pause'),
    (datetime.time(9, 45), 3),
    (datetime.time(10, 30), 4),
    (datetime.time(11, 15), 'Pause'),
    (datetime.time(11, 30), 5),
    (datetime.time(12, 15), 6),
    (datetime.time(13, 0),  'Pause'),
    (datetime.time(13, 15), 7),
    (datetime.time(14, 0), 8)
    ]
stunden_masch.extend(stunden_abend)

def print_stunde(stunden):
    now = datetime.datetime.now().time()

    for i, (stunden_beginn, stunde) in enumerate(stunden):

        if i + 1 < len(stunden):
            next_stundenbeginn, _ = stunden[i + 1]

            if stunden_beginn <= now < next_stundenbeginn:
                std = str(next_stundenbeginn.minute).zfill(2)
                print(stunde, f'bis {next_stundenbeginn.hour}:{std}')
                return

        else: # keine nächste Stunde
            print("Tagesende")

if __name__ == "__main__":
    print("Allgemeine Stundentafel: ", end="")
    print_stunde(stunden_allgemein)
    print("Stundentafel Maschinenbau: ", end="")
    print_stunde(stunden_masch)
