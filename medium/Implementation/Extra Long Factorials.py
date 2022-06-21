# https://www.hackerrank.com/challenges/extra-long-factorials/problem
# 분류 : Implementation
# 난이도 : meduim
# 풀이시간 7분

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

factorials = {1: 1, 2: 2}

def factorial(n):
    factorials[n] = factorials[n-1] * n

def extraLongFactorials(n):
    
    for i in range(2, n+1):
        factorial(i)
    
    return factorials[n] 


if __name__ == '__main__':
    n = 25
    result = extraLongFactorials(n)
    print(result)
