#!/usr/bin/python3
""" pthon exceptins"""
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            y += 1
        except (TypeError, ValueError):
            continue
    print()
    return y
