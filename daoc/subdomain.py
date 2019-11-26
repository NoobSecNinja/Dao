#!/usr/bin/env python3

import sys
import os
import requests as rq

class Subdomain:
    def __init__(self, domain):
        self.domain = domain

    def sublist(self):
        return list(self.domain)