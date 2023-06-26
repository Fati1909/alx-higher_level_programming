#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result."""

    try:
        ope = a / b
    except (TypeError, ZeroDivisionError):
        ope = None
    finally:
        print("Inside result: {}".format(ope))
    return (ope)
