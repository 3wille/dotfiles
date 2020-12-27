#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import sys
import urllib.error

try:
    response = urlopen("http://v4.ipv6-test.com/api/myip.php")
    s = response.read().decode('utf-8')
    print("🌎" + s)
    sys.exit(0)
except urllib.error.URLError:
    print("🌎")
    sys.exit(1)

