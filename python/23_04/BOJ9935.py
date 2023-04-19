# 문자열 폭발

import sys
from collections import deque

input = sys.stdin.readline
stack = deque()
inputString = input().strip()
bomb = input().strip()

i = 0
n = len(bomb)
for s in inputString:
    if s == bomb[i]:
        if i == n - 1:
            for _ in range(n - 1):
                stack.pop()
            if stack:
                i = stack[-1][1]
        else:
            i += 1
            stack.append([s, i])
    else:
        i = 0
        if s == bomb[0]:
            i = 1
        stack.append([s, i])

print("".join([x[0] for x in stack]) if stack else "FRULA")
    
# https://www.acmicpc.net/problem/9935