#!/usr/bin/python3
"""class MyList that inherits from list."""

class MyList(list):
    """implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """prints the list in sorted ascending sort."""
        print(sorted(self))
