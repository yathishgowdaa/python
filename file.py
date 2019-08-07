#!/usr/bin/python
from __future__ import print_function





def print_star(x):
    for row in range(1, x + 1):
        for column in range(1, row + 1):
            print(column, end=' ')
        print("")



num = 5
print_star(num)
