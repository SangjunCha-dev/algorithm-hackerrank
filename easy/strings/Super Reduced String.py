# 문제링크: https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=true
# 분류 : Strings
# 난이도: easy
# 풀이시간: 11분


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# 인접한 문자가 동일하고 짝수개수인 경우 삭제
# 삭제후 붙은 문자가 위의 조건과 동일하면 삭제 반복
# 모든 문자가 삭제되면 "Empty String" 반환

def superReducedString(s):
    s = list(s)
    is_remove = True
    while is_remove:
        is_remove = False
    
        i = len(s)-2
        while -1 < i:
            if s[i] == s[i+1]:
                del s[i:i+2]
                is_remove = True
                i -= 2
            else:
                i -= 1

    answer = ''.join(s) if s else "Empty String"
    return answer

if __name__ == '__main__':

    print(f"======================================")

    s = "aaabccddd"

    result = superReducedString(s)

    answer = "abd"
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")