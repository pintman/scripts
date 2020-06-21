#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 2:
        print("Maximale Punktzahl angeben")
        exit(1)
    max_p = int(sys.argv[1])
    print("Note\tab")
    print("----\t--")

    for note, faktor in [(1, 0.92),
                           (2, 0.81),
                           (3, 0.67),
                           (4, .5),
                           (5, .3),
                           (6, 0)]:
        print(note, "\t", round(faktor*max_p, 1))


if __name__ == '__main__':
    main()
