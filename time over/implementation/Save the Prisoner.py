# 문제링크: https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: easy
# 풀이시간: 22분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n  # 의자 개수
#  2. INTEGER m  # 간식 개수
#  3. INTEGER s  # 시작할 의자 번호
#

# 순차적으로 번호가 매겨진 의자가 원형 테이블에 있다
# 마지막 간식을 받은 의자 번호 반환

def saveThePrisoner(n, m, s):
    m = m % n
    s = m-1+s
    s = s % n
    s = s if s else n
    return s

if __name__ == '__main__':

    print(f"======================================")

    n = 5
    m = 2
    s = 1

    result = saveThePrisoner(n, m, s)

    answer = 2
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 5
    m = 10
    s = 1

    result = saveThePrisoner(n, m, s)

    answer = 1
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 3
    m = 7
    s = 3

    result = saveThePrisoner(n, m, s)

    answer = 3
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")