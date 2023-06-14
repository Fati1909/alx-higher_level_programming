#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    elist = list(a_dictionary.keys())
    elist.sort()
    for i in elist:
        print("{}: {}".format(i, a_dictionary.get(i)))
