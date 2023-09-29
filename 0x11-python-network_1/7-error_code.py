#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL"""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print(f"Error code: {response.status_code}")
