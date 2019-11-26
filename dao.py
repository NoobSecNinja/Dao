#!/usr/bin/env python3

import os
import sys

# Peohibit from writing bytecodes
sys.dont_write_bytecode = True

# Core Modules
from daoc.subdomain import Subdomain

# Screen Functionalities
from daoc.view import screen as scr

# Third-Party Modules
from modules.assetfinder import AssertFinder

def subdomain(domain):
    # sub = Subdomain(domain)
    # subs = sub.sublist()
    # scr.result(subs)

    # Assetfinder
    sub = AssertFinder(domain)
    sub.find()
    # sub.check()

def check_all():
    pass

def help():
    print("[-] I'm not available!")

def main():
    pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        if sys.argv[1] in ('-d', '-domain'):
            check_all()
        elif sys.argv[1] in ('-s', '-sub'):
            domain = sys.argv[2]
            subdomain(domain)
