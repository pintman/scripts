#!/usr/bin/env python3
"""
Allows for importing Export CSV-Files from Postbank into
ledgers (https://ledger-cli.org) file format.
"""
import csv
import sys

encoding = "ISO8859-15"
file = sys.argv[1]
datecol = 1
payeecol = 5
notecol = 3
amountcol = 6
account="PB"

template = """{date} * {payee}
    ; {note}
    ; imported from line
    ; {orig}
    {account}      {amount}€
    Imported:Unknown
"""

def uptospace(string):
    return string[0:string.find(" ")]

def date_de_to_iso(date):
    """Convert date in german notation into iso form.
    >>> date_de_to_iso("01.12.2033")
    '2033-12-01'
    """
    year = date[6:]
    mon = date[3:5]
    day = date[:2]

    return year + "-" + mon + "-" + day

def main():
    #print("opening", file)
    with open(file, encoding=encoding) as f:
        rows = csv.reader(f, delimiter=";")
        for r in rows:
            print(template.format(
                date=date_de_to_iso(r[datecol]),
                payee=r[payeecol],
                note=r[3],
                orig=" ".join(r),
                account="PB",
                amount=uptospace(r[amountcol])))
                
            

if __name__ == "__main__":
    main()
