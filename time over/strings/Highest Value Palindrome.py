# 문제링크: https://www.hackerrank.com/challenges/richie-rich/problem?isFullScreen=true
# 분류 : Implementation
# 난이도: meduim
# 풀이시간: 시간초과

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

# 왼쪽 또는 오른쪽에서 같은 값을 가진 문자열
# 지정할 수 있는 숫자와 최대 변경 수를 나타내는 문자열이 표시
# 한 번에 한 자리씩 문자열을 변경하여 변경 수 제한이 있는 최대 수의 문자열 표현을 만듬
# 문자열의 길이는 변경되지 않을 수 있으므로 테스트에서 의 모든 상위 자리 중 왼쪽 자리를 고려해야함

# 가능한 한 큰 숫자의 문자열을 만들거나 문자열을 만들 수 없는 경우 문자열 '-1'을 반환


def highestValuePalindrome(s, n, k):
    s = list(s)
    edited = {i: False for i in range(n)}

    # 왼쪽과 오른쪽의 같은 숫자를 가진 문자열 생성
    low = 0
    high = n-1
    while low < high:
        if s[low] != s[high]:
            if s[high] < s[low]:
                s[high] = s[low]
                edited[high] = True
            else:
                s[low] = s[high]
                edited[low] = True
            k -= 1

        low += 1
        high -= 1

        if k < 0:
            return '-1'

    # k(수정가능한 횟수) 남은 경우 가장 큰수로 변환
    low = 0
    high = n-1
    while (low <= high) and (0 < k):
        if (s[low] != '9') and (0 < k):
            if edited[low] or edited[high]:
                s[low], s[high] = '9', '9'
                if not edited[low]:
                    k -= 1
                if not edited[high]:
                    k -= 1
            elif 1 < k:
                s[low], s[high] = '9', '9'
                k -= 2
            elif low == high:
                s[low] = '9'
                k -= 1

        low += 1
        high -= 1

    return ''.join(s)

if __name__ == '__main__':

    print(f"======================================")

    n = 4  # 정수 문자열 길이
    k = 1  # 허용되는 최대 변경 수
    s = '3943'  # 정수 문자열

    result = highestValuePalindrome(s, n, k)

    answer = '3993'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 6  # 정수 문자열 길이
    k = 3  # 허용되는 최대 변경 수
    s = '092282'  # 정수 문자열

    result = highestValuePalindrome(s, n, k)

    answer = '992299'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    n = 4  # 정수 문자열 길이
    k = 1  # 허용되는 최대 변경 수
    s = '0011'  # 정수 문자열

    result = highestValuePalindrome(s, n, k)

    answer = '-1'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    s = '9711319'
    n = 7
    k = 4

    result = highestValuePalindrome(s, n, k)

    answer = '9991999'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    s = '329'
    n = 3
    k = 2

    result = highestValuePalindrome(s, n, k)

    answer = '999'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    s = '10011'
    n = 5
    k = 1

    result = highestValuePalindrome(s, n, k)

    answer = '11011'
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")