#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list."""
    mul = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mul.append(True)
        else:
            mul.append(False)


    return (mul)
