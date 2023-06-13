#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    mx = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > mx:
            mx = my_list[i]
            

    return (big)
