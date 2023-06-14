#!/usr/bin/python3
def number_keys(a_dictionary):
    dig = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        dig += 1

    return (dig)
