# 문제링크: https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?isFullScreen=true
# 분류 : Greedy
# 난이도: easy
# 풀이시간: 9분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# arr 배열의 각 요소 차이값 중 최소 절대값을 찾아 반환

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_value = int(1e9)
    for i in range(len(arr)-1):
        abs_value = abs(arr[i] - arr[i+1])
        if abs_value < min_value:
            min_value = abs_value

    return min_value


if __name__ == '__main__':

    print(f"======================================")

    arr = [3, -7, 0]

    result = minimumAbsoluteDifference(arr)

    answer = 3
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]

    result = minimumAbsoluteDifference(arr)

    answer = 1
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")