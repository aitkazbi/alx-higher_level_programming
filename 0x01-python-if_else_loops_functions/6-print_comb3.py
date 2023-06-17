#!/usr/bin/python3

for i in range(0, 9):
    for num in range(1, 10):
        if i < num:
            if i == 8:
                print("{}{}".format(i, num))
            else:
                print("{}{},".format(i, num), end=" ")
