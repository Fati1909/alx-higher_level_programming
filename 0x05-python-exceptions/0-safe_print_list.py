#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list.
    Args:
      my_list (list): list to print.
      x (int): num of elements to print.

    Returns:
      num of elements printed.
    """

    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
