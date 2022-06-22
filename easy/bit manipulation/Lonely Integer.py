# 문제링크: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true
# 분류 : Bit Manipulation
# 난이도: easy
# 풀이시간: 15분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# 배열 a의 고유한 요소를 찾아 반환


def lonelyinteger(a):
    answer = None
    data = {}
    for v in a:
        data[v] = False if v in data else True

    for k, v in data.items():
        if v:
            answer = k
            break

    return answer


if __name__ == '__main__':

    print(f"======================================")

    a = [1]

    result = lonelyinteger(a)

    answer = 1
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    a = [1, 1, 2]

    result = lonelyinteger(a)

    answer = 2
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    a = [1, 2, 1, 1]

    result = lonelyinteger(a)

    answer = 2
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")
