#!/usr/bin/python3

from decimal import DivisionByZero, DivisionImpossible


def safe_print_division(a, b):
    try:
        division = a / b
    except (ZeroDivisionError, FloatingPointError):
        
        division = None
        
    finally:
       print("Inside result: {}".format(DivisionImpossible))
       return DivisionByZero
