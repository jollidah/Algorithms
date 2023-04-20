# 탈출

import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n , m = map(int, input().split())
wall = [[False for _ in range(m)] for _ in range(n)]
waterQueue = deque()
sq = deque()
svisit = [[False for _ in range(m)] for _ in range(n)]

for y in range(n):
    tmp = input().strip()
    for x in range(m):
        if tmp[x] == "*":
            wall[y][x] = True
            svisit[y][x] = True
            waterQueue.append([y, x])
        elif tmp[x] == "X":
            wall[y][x] = True
            svisit[y][x] = True
        elif tmp[x] == "S":
            sy, sx = y, x
        elif tmp[x] == "D":
            wall[y][x] = True
            ty, tx = y, x
q = deque()
for y, x in waterQueue:
    q.append([True, y, x, 0])
q.append([False, sy, sx, 0])
while q:
    water, y, x, t = q.popleft()
    if water:
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0 and not wall[tmpY][tmpX]:
                wall[tmpY][tmpX] = True
                svisit[tmpY][tmpX] = True
                q.append([True, tmpY, tmpX, t + 1])
    else:
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0 and not svisit[tmpY][tmpX]:
                if ty == tmpY and tx == tmpX:
                    print(t + 1)
                    exit(0)
                else:
                    svisit[tmpY][tmpX] = True
                    q.append([False, tmpY, tmpX, t + 1])
print("KAKTUS")

# https://www.acmicpc.net/problem/3055