# 최솟값 찾기

import sys
from collections import deque

input = sys.stdin.readline
n , l = map(int, input().split())
seq = list(map(int, input().split()))
slide = []
dq = deque()

rp = 0
tl = l
while tl > 0:
    tl -= 1
    while dq and dq[-1] > seq[rp]:
        dq.pop()
    dq.append(seq[rp])    
    print(dq[0], end = ' ')
    rp += 1
lp = 0

while rp < n:
    # print(dq)
    if seq[lp] == dq[0]:
        dq.popleft()
    while dq and dq[-1] > seq[rp]:
        dq.pop()
    dq.append(seq[rp])
    print(dq[0], end = ' ')
    rp += 1
    lp += 1

# https://www.acmicpc.net/problem/11003