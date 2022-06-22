# 문제링크: https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: easy
# 풀이시간: 14분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s              # 집의 왼쪽끝 위치
#  2. INTEGER t              # 집의 오른쪾끝 위치
#  3. INTEGER a              # 사과 나무 위치
#  4. INTEGER b              # 오렌지 나무 위치
#  5. INTEGER_ARRAY apples   # 사과나무로부터 사과가 떨어진 위치들
#  6. INTEGER_ARRAY oranges  # 오렌지나무로부터 오렌지가 떨어진 위치들
#

# 집의 위치에 떨어진 사과와 오렌지의 개수 구하기

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # apple tree
    apple_cnt = 0
    for apple in apples:
        if s <= (apple + a) <= t:
            apple_cnt += 1
    print(apple_cnt)

    # orange tree
    orange_cnt = 0
    for orange in oranges:
        if s <= (orange + b) <= t:
            orange_cnt += 1
    print(orange_cnt)

if __name__ == '__main__':

    # print(f"======================================")

    # s = 7
    # t = 11

    # a = 5
    # b = 15

    # apples = [-2, 2, 1]
    # oranges = [5, -6]

    # countApplesAndOranges(s, t, a, b, apples, oranges)

    # print(1)
    # print(1)

    print(f"======================================")

    s = 7
    t = 11

    a = 15
    b = 5

    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)

    print(0)
    print(1)

    print(f"======================================")
