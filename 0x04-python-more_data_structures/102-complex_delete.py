#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    elist = list(a_dictionary.keys())

    for value_dic in elist:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return (a_dictionary)
