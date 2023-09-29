#!/usr/bin/python3
"""script that takes in a URL and an email address"""
import sys
import requests


if __name__ == "__main__":
    playload = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=playload)
    print(response.text)
