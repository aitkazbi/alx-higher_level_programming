#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in range(len(my_list)):
        if my_list[idx] < 0 or idx >= len(my_list):
        return None
