#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""

def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = [".", "?", ":"]
    result = ""

    for char in text:
        result += char
        if char in characters:
            result += "\n\n"

    rows = result.splitlines()
    for row in rows:
        print(row.strip())
