#!/usr/bin/python3

# islower - Check for lowercase character
# Return - True if c is lowercase, if otherwise False

def islower(c):
    if (ord(c) > 96 and ord(c) < 123):
        return True
    else:
        return False
