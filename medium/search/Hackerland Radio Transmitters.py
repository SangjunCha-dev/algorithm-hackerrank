# 문제링크: https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem?isFullScreen=true
# 분류 : Search
# 난이도: meduim
# 풀이시간: 32분

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

# 해커 랜드지도(x)와 전송 범위(k)가 주어지면 모든 집이 적어도 하나의 송신기 범위 내에 있도록 최소 송신기 수를 결정
# 각 송신기는 기존 주택 위에 설치

def hackerlandRadioTransmitters(x, k):
    x.sort()
    front_pos = x[0]
    setup_pos = x[0]
    answer = 1

    for v in x[1:]:
        # 송신기 설치 위치 조정
        if v-k <= front_pos:
            setup_pos = v

        # 송신기 범위 이탈시
        if setup_pos + k < v:
            front_pos = v
            setup_pos = v
            answer += 1

    return answer


if __name__ == '__main__':

    print(f"======================================")

    k = 1
    x = [1, 2, 3, 4, 5]

    result = hackerlandRadioTransmitters(x, k)

    answer = 2
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")

    k = 2
    x = [7, 2, 4, 6, 5, 9, 12, 11]

    result = hackerlandRadioTransmitters(x, k)

    answer = 3
    print(f"{result}: {result==answer} / answer: {answer}")

    print(f"======================================")