# 문제링크: https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true
# 분류 : Sorting
# 난이도: meduim
# 풀이시간: 40분

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

# 카운트 정렬을 사용하여 index 정수와 관련된 문자열 목록을 정렬
# 2개의 문자열이 같은 정수에 관련지어져 있는 경우 원래의 순서로 유지
# arr의 절반에 해당하는 전반부의 문자열을 '-'문자로 치환

def countSort(arr):
    for ar in arr[:len(arr)//2]:
        ar[1] = '-'
    
    arr.sort(key=lambda x: int(x[0]))
    answer = ' '.join(map(str, [v[1] for v in arr]))
    print(answer)


if __name__ == '__main__':
    arr = [
        [0, 'ab'],
        [6, 'cd'],
        [0, 'ef'],
        [6, 'gh'],
        [4, 'ij'],
        [0, 'ab'],
        [6, 'cd'],
        [0, 'ef'],
        [6, 'gh'],
        [0, 'ij'],
        [4, 'that'],
        [3, 'be'],
        [0, 'to'],
        [1, 'be'],
        [5, 'question'],
        [1, 'or'],
        [2, 'not'],
        [4, 'is'],
        [2, 'to'],
        [4, 'the'],
    ]

    countSort(arr)

    answer = '- - - - - to be or not to be - that is the question - - - -'
    print(answer)