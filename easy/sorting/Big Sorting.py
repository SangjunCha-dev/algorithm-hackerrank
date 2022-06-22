# 문제링크: https://www.hackerrank.com/challenges/big-sorting/problem?isFullScreen=true
# 분류 : Sorting
# 난이도: easy
# 풀이시간: 8분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

# 문자열 정수 배열을 입력받아 숫자 오름차순으로 정렬한다.
# 반환할때 문자열 정수 배열로 반환한다.


def bigSorting(unsorted):
    unsorted.sort(key=lambda x: int(x))
    return unsorted

if __name__ == '__main__':

    print(f"======================================")

    unsorted = ["31415926535897932384626433832795", "1", "3", "10", "3", "5"]

    result = bigSorting(unsorted)

    answer = ["1", "3", "3", "5", "10", "31415926535897932384626433832795"]
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")