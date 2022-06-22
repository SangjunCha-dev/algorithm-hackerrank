# 문제링크: https://www.hackerrank.com/challenges/icecream-parlor/problem?isFullScreen=true
# 분류 : Search
# 난이도: easy
# 풀이시간: 10분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

# 모든 돈(m)을 지불할 두 요소 선택(arr)

def icecreamParlor(m, arr):
    n = len(arr)
    answer = []
    for i in range(n-1):
        cost = m - arr[i]
        for j in range(i+1, n):
            if arr[j] == cost:
                answer = [i+1, j+1]
                return answer
    return answer

if __name__ == '__main__':

    print(f"======================================")

    m = 4
    arr = [1, 4, 5, 3, 2]

    result = icecreamParlor(m, arr)

    answer = [1, 4]
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    m = 4
    arr = [2, 2, 4, 3]

    result = icecreamParlor(m, arr)

    answer = [1, 2]
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")