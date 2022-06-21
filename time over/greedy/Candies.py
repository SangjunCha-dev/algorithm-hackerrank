# 문제링크: https://www.hackerrank.com/challenges/candies/problem?isFullScreen=true
# 분류 : Greedy
# 난이도: meduim
# 풀이시간: 시간 초과 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n          # 학생 수
#  2. INTEGER_ARRAY arr  # 각 학생의 평점
#

# 각 학생은 최소 1개 이상의 사탕을 받음
# 학생이 나란히 앉았을 때 더 높은 값은 더 많은 사탕을 받아야 함



def candies(n, arr):
    point = [1 for _ in range(n)]

    for i in range(1, n):
        if arr[i-1] < arr[i]:
            point[i] = point[i-1] + 1

    for i in range(n-2, -1, -1):
        if (arr[i+1] < arr[i]) and (point[i] <= point[i+1]):
            point[i] = point[i+1] + 1

    return sum(point)


if __name__ == '__main__':

    print(f"======================================")

    n = 3
    arr = [1, 2, 2]

    result = candies(n, arr)

    answer = 4
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 6
    arr = [4, 6, 4, 5, 6, 2]

    result = candies(n, arr)

    answer = 10  # [1, 2, 1, 2, 3, 1]
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 10
    arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]

    result = candies(n, arr)

    answer = 19
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 3
    arr = [3, 2, 1]

    result = candies(n, arr)

    answer = 6
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")
