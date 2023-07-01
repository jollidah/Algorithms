# 문자열 폭발

import sys
from collections import deque

inp = sys.stdin.readline
inputString = inp().strip()
bombStr = inp().strip()
cnt = 0         # 해당 문자열 기준 count 저장
target = bombStr[0] 
stack = deque()

# 폭발 함수
def bomb():
    for _ in range(len(bombStr)):
        stack.pop()

for s in inputString:
    if s == target:     # 타겟과 같다면 cnt + 1
        cnt += 1
    elif s == bombStr[0]:   # 타겟과 다르지만 시작하는 str이라면 1부터
        cnt = 1
    else:
        cnt = 0         # cnt 초기화
    stack.append([s, cnt])
    if cnt == len(bombStr):
        bomb()
        if stack:
            cnt = stack[-1][1]
        else:
            cnt = 0
    target = bombStr[cnt]   # target 업데이트

print("".join(list(map(lambda x : x[0], stack))) if stack else "FRULA")

# https://www.acmicpc.net/problem/9935