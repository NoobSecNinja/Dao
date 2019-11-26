#!/usr/bin/env python3

# Assetfinder by Tomnomnom
# github.com/tomnomnom/assetfinder
# assetfinder --subs-only domain |tee output_file


import os
import sys
from subprocess import run
from subprocess import DEVNULL, STDOUT, PIPE

from daoc.subdomain import Subdomain

class AssertFinder(Subdomain):
    def check(self):
        status = run(["assetfinder", "--help"], stdout=DEVNULL, stderr=STDOUT)
        if status != 0:
            run(["go", "get", "github.com/tomnomnom/assetfinder"],
                stdout=DEVNULL, stderr=STDOUT)
        else:
            return True

        return 0

    def find(self):
        cwd = os.getcwd()
        # "|tee", f"{cwd}/output/subdomain/{self.domain}/assetfinder.txt",
        status = run(["assetfinder", "--subs-only", f"{self.domain}"], stdout=PIPE)
        data = status.stdout
        out = f"{cwd}/output/subdomain/{self.domain}"
        if not os.path.exists(out):
            os.mkdir(f"{cwd}/output/subdomain/{self.domain}")
        with open(f"{cwd}/output/subdomain/{self.domain}/assetfinder.txt", "w") as f:
            f.write(data.decode('ascii'))
