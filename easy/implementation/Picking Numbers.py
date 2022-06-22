# 문제링크: https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: easy
# 풀이시간: 18분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# 정수 배열(a)이 주어지면 두 요소간의 차이 1이거나 없는 배열 중 가장 긴 배열의 길이 값 반환
# [1, 1, 2, 2, 3, 4, 4, 5, 5, 5] 주어질때
# [1, 1, 2, 2], [2, 2, 3] 이런식으로만 묶여진다

def pickingNumbers(a):
    data = {}
    for v in a:
        if v in data:
            data[v] += 1
        else:
            data[v] = 1


    keys = list(data.keys())
    keys.sort()

    max_cnt = data[keys[0]]
    for i in range(1, len(keys)):
        if max_cnt < data[keys[i]]:
            max_cnt = data[keys[i]]

        v = abs(keys[i] - keys[i-1])
        if v <= 1:
            total_cnt = data[keys[i]] + data[keys[i-1]]
            if max_cnt < total_cnt:
                max_cnt = total_cnt

    return max_cnt

if __name__ == '__main__':

    print(f"======================================")

    a = [4, 6, 5, 3, 3, 1]

    result = pickingNumbers(a)

    answer = 3
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")
