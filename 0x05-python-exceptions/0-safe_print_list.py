#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            total += 1
    except IndexError:
    
         print()  
    return total
