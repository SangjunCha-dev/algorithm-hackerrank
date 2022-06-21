# 문제링크: https://www.hackerrank.com/challenges/angry-children/problem?isFullScreen=true
# 분류 : Greedy
# 난이도: meduim
# 풀이시간: 23분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

# arr의 요소로부터 길이 k의 배열을 생성하여 min max 값 차이의 최소값 구하기
# 정수가 고유하지 않을 수 있음


def maxMin(k, arr):
    arr.sort()

    min_value = arr[-1]
    for i in range(len(arr)-k+1):
        value = arr[i+k-1] - arr[i]
        if value < min_value:
            min_value = value

    return min_value


if __name__ == '__main__':

    print(f"======================================")

    k = 3
    arr = [10, 100, 300, 200, 1000, 20, 30]

    result = maxMin(k, arr)

    answer = 20
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    k = 2
    arr = [1, 2, 1, 2, 1]

    result = maxMin(k, arr)

    answer = 0
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")