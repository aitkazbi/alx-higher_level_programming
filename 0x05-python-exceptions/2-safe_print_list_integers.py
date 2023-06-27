#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
      
            total += 1
    except (ValueError, TypeError):
        pass
    finally:
      print ()
      return total
