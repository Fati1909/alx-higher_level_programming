#!/usr/bin/python3

def magic_calculation(a, b):
    ope = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                ope += a ** b / i
        except:
            ope = b + a
            break
    return (ope)
