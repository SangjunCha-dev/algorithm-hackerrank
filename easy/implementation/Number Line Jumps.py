# 문제링크: https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: easy
# 풀이시간: 15분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1  # 캥거루1 위치
#  2. INTEGER v1  # 캥거루1 1회 이동거리
#  3. INTEGER x2  # 캥거루2 위치
#  4. INTEGER v2  # 캥거루2 1회 이동거리
#

# 캥거루1과 2이 같은 점프횟수를 가질때 같은곳에서 만날수 있는지 여부 반환
# 결과값을 "NO" or "YES" 반환


def kangaroo(x1, v1, x2, v2):
    if (x1 < x2) and (v1 <= v2):
        return "NO"

    while x1 < x2:
        x1 += v1
        x2 += v2
    
    return "YES" if x1 == x2 else "NO"


if __name__ == '__main__':

    print(f"======================================")

    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    result = kangaroo(x1, v1, x2, v2)

    answer = "YES"
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    x1 = 0
    v1 = 2
    x2 = 5
    v2 = 3

    result = kangaroo(x1, v1, x2, v2)

    answer = "NO"
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    x1 = 0
    v1 = 0
    x2 = 5
    v2 = 0

    result = kangaroo(x1, v1, x2, v2)

    answer = "NO"
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")