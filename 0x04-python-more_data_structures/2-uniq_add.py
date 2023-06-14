#!/usr/bin/python3
def uniq_add(my_list=[]):
    elist = set(my_list)
    dig = 0

    for i in elist:
        dig += i

    return (dig)
