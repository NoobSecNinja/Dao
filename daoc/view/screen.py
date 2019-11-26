#!/usr/bin/env python3

import os
import sys

def banner():
    return "\tGreetings from \"Dao\" Team!\n@2019\n"

def result(data):
    print(f"[+] Total Subdomains: {len(data)}")
    for item in data:
        print(f"[+] Subdomain: {item}")