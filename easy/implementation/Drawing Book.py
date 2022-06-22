# 문제링크: https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: easy
# 풀이시간: 16분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n  # 책의 페이지 수
#  2. INTEGER p  # 찾아야 할 페이지 번호
#

# 책의 앞면이나 뒷면에서 페이지를 넘기 시작할 수 있다
# 항상 한 번에 한 페이지씩 넘긴다
# 1페이지는 항상 오른쪽에 있다

# 페이지를 찾을 수 있는 페이지를 넘긴 횟수 반환
# 맨앞부터 찾거나 맨뒤부터 찾음

def pageCount(n, p):
    front_cnt = p//2

    back_cnt = n-p if n%2 == 0 else n-p-1
    back_cnt = (back_cnt//2) + (back_cnt%2)

    answer = front_cnt if front_cnt < back_cnt else back_cnt
    return answer

if __name__ == '__main__':

    print(f"======================================")

    n = 5
    p = 3

    result = pageCount(n, p)

    answer = 1
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 6
    p = 2

    result = pageCount(n, p)

    answer = 1
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 5
    p = 4

    result = pageCount(n, p)

    answer = 0
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")