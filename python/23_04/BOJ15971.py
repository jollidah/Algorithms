# 두 로봇

import sys
from collections import deque

input = sys.stdin.readline

n, r1, r2 = map(int, input().split())
if r1 == r2:
    print(0)
    exit(0)
toVisit = [True for _ in range(n + 1)]
vertex = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    vertex[a].append([b, c])
    vertex[b].append([a, c])
dq = deque()
dq.append([r1, 0, 0])
toVisit[r1] = False

while True:
    pos, td, md = dq.popleft()
    # print(pos, td, md)
    for next, w in vertex[pos]:
        tmpTd = td
        tmpMd = md
        if md < w:
            tmpTd += md
            tmpMd = w
        else:
            tmpTd += w        
        if next == r2:
            print(tmpTd)
            exit(0)
        elif toVisit[next]:
            toVisit[next] = False
            dq.append([next, tmpTd, tmpMd])

# https://www.acmicpc.net/problem/15971