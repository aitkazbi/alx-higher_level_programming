#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    total = 0
    try:
        for i in my_list:
            if isinstance(i, int):
                print("{:d}".format(i), end="")
                total += 1
                if total == x:
                    break
    except (ValueError, TypeError):
        pass
    finally:
      print ()
      return total
