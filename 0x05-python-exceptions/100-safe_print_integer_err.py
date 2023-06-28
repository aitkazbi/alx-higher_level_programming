#!/usr/bin/python3
"""print An integer"""
def safe_print_integer_err(value):

   try:
        print("{:d}".format(value))
        return True
   except :
        print("{} is not an integer ".format(value))
        return False
