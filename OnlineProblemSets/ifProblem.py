#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if (n%2) != 0:
        print('Weird 2', n,n%2)
    elif (n%2) == 0 and n>=2 and n<=5:
        print('Not Weird 2', n,n%2)
    elif (n%2) == 0 and n>=6 and n<=20:
        print('Weird 1', n,n%2)
    elif (n%2) == 0 and n>20:
        print('Not Weird 1', n,n%2)
    else:
        print('Weird')
        