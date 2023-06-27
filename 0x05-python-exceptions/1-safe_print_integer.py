#!/usr/bin/python3

def safe_print_integer(value):
    try:
        int(value)
        value = True
    except ValueError:
        value = False

    print("{:d}".format())
