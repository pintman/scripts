#!/usr/bin/env python3
"""
Allows for importing Export CSV-Files from Postbank into
ledgers (https://ledger-cli.org) file format.
"""
import csv
import sys
import configparser
import os

# some configurations
# encoding of the import file
encoding = "ISO8859-15"
# filename to be use for import
file = sys.argv[1]
# config file for mappings
configfile = os.environ["HOME"] + "/.pb2ledgerrc"
# columns for date, payee, note and amount information
datecol = 1
payeecol = 5
notecol = 3
amountcol = 6
# account to book against
account="Bestand:PB"
account_unknown="Ausgaben:Unknown"

# template for the output
template = """{date} * {payee}
    ; {note}
    ; imported from line
    ; {orig}
    {account}      {amount}€
    {account2}
"""


config = configparser.ConfigParser()
config.read(configfile)

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

def account_for_payee(payee):
    """Check if there is an account defined for this payee.
    The format ist as follows:
    KARSTADT = Ausgaben:Haushalt

    Multiple account can be defined for payment with known amounts
    MIETER = 700€@Ausgaben:Miete 250€@Ausgaben:Nebenkosten
    """ 
    key = "payee2account"
    if key in config and payee in config[key]:
        acc = config[key][payee]
        if " " in acc:
            # there are multiple account defined
            # split and add them all
            accs = acc.split(" ")
            res = ""
            for a in accs:
                if "@" in a:
                    am,account = a.split("@")
                    res += account +"  " + am + "\n    "
            return res
        
        else:
            return config[key][payee]
    else:
        return account_unknown
    
def main():
    with open(file, encoding=encoding) as f:
        rows = csv.reader(f, delimiter=";")
        for r in rows:
            print(template.format(
                date=date_de_to_iso(r[datecol]),
                payee=r[payeecol],
                note=r[3],
                orig=" ".join(r),
                account="PB",
                account2=account_for_payee(r[payeecol]),
                amount=uptospace(r[amountcol])))
                
            

if __name__ == "__main__":
    main()
