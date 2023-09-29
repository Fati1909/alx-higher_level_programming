#!/usr/bin/python3
"""script that takes in a URL"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as resp:
        header = dict(resp.headers)
        print(header.get("X-Request-Id"))
