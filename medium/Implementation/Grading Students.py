# 문제링크: https://www.hackerrank.com/challenges/grading/problem
# 분류 : Implementation
# 난이도 : meduim
# 풀이시간: 14분

# grade 38 보다 작으면 변환하지 않음
# 일의자리가 5의 배수보다 3미만으로 작을때 5의 배수로 올림

#!/bin/python3

import math
import os
import random
import re
import sys

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.

def gradingStudents(grades):
    for i in range(len(grades)):
        grade = grades[i]
        if grade < 38:
            continue

        one_digits = grade % 10
        one_digits = one_digits if one_digits < 5 else one_digits - 5

        if 3 <= one_digits:
            grades[i] += (5 - one_digits)

    return grades

if __name__ == '__main__':
    
    grades = [73, 67, 38, 33]

    result = gradingStudents(grades)
    answer = [75, 67, 40, 33]

    print(f"{answer}: {result==answer}")
