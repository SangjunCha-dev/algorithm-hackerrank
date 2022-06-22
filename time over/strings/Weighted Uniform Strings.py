# 문제링크: https://www.hackerrank.com/challenges/weighted-uniform-string/problem?isFullScreen=true
# 분류 : Strings
# 난이도: easy
# 풀이시간: 
# 시작 초과



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

# 문자열 a~z가 있고 각각의 가중치는 1~26이다.
# 문자열의 가중치는 문자의 가중치의 합이다.
# s 문자열에 대한 가중치가 존재하는지 여부를 "Yes" or "No"으로 반환한다.


def weightedUniformStrings(s, queries):
    answer = []
    scores = set()
    prev_s = None
    re_cnt = 0

    for v in s:
        if v != prev_s:
            prev_s = v
            re_cnt = 0
        re_cnt += 1

        score = ord(v) - ord('a') + 1
        scores.add(score * re_cnt)

    for v in queries:
        if v in scores:
            answer.append("Yes")
        else:
            answer.append("No")

    return answer


if __name__ == '__main__':
    print(f"======================================")

    s = "abbcccdddd"
    queries = [1, 7, 5, 4, 15]

    result = weightedUniformStrings(s, queries)

    answer = ['Yes', 'No', 'No', 'Yes', 'No']
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")
