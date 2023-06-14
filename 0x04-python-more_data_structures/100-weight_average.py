#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    dig = 0
    las = 0

    for i in my_list:
        dig += i[0] * i[1]
        las += i[1]

    return (dig / las)
