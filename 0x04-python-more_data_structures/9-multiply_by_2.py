#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = a_dictionary.copy()
    elist = list(dic.keys())

    for i in elist:
        dic[i] *= 2

    return (dic)
