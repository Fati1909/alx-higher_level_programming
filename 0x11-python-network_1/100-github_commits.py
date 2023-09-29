#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"
    resp = requests.get(url.format(argv[2], argv[1]))
    res = resp.json()
    try:
        for j in range(0, 10):
            print(f"{res[j].get('sha')}: \
{res[j].get('commit').get('author').get('name')}")
    except IndexError:
        pass
