# 안전 영역

import sys
import heapq
from collections import deque

inp = sys.stdin.readline
n = int(inp())
pq = []
cnt = 1
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
water = [[False for _ in range(n)] for _ in range(n)]
for y in range(n):
    tmp = list(map(int, inp().split()))
    for x in range(n):
        heapq.heappush(pq, [tmp[x], y, x])
h, y, x = heapq.heappop(pq)
height = h
water[y][x] = True

def print_grid():
    for y in range(n):
        for x in range(n):
            if water[y][x] == False:
                print(1, end = " ")
            else: 
                print(0, end = " ")
        print()
    print()

while pq:
    h, y, x = heapq.heappop(pq)
    if h != height:
        visit = [[False for _ in range(n)] for _ in range(n)]
        tmpCnt = 0
        for ty in range(n):
            for tx in range(n):
                if not water[ty][tx] and not visit[ty][tx]:
                    tmpCnt += 1
                    q = deque()
                    q.append([ty, tx])
                    visit[ty][tx] = True
                    while q:
                        py, px = q.popleft()
                        for d in range(4):
                            tmpY = py + dy[d]
                            tmpX = px + dx[d]
                            if n > tmpY >= 0 and n > tmpX >= 0\
                                and not visit[tmpY][tmpX] and not water[tmpY][tmpX]:
                                visit[tmpY][tmpX] = True
                                q.append([tmpY, tmpX])
        cnt = max(cnt, tmpCnt)
        height = h
    water[y][x] = True
print(cnt)

# https://www.acmicpc.net/problem/2468