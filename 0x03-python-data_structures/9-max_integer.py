#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None

    max_num = my_list[0]
    for i in my_list:
        if i > max_num:
            max_num = i
            

    return max_num
