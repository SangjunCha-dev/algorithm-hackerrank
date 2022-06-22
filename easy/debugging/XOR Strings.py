# 문제링크: https://www.hackerrank.com/challenges/strings-xor/problem?isFullScreen=true
# 분류 : Debugging
# 난이도: easy
# 풀이시간: 15분 

# 최대 3줄만 수정 가능

def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))