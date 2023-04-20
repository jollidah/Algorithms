# 아기 상어

import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
n = int(input().strip())
grid = []
sharksize = 2
cnt = 0
time = 0

for y in range(n):
    grid.append(list(map(int, input().split())))
    for x in range(n):
        if grid[y][x] == 9:
            sy, sx = y, x
            grid[y][x] = 0

canEat = True
while canEat:
    if cnt == sharksize:
        cnt = 0
        sharksize += 1
    visit = [[False for _ in range(n)] for __ in range(n)]
    visit[sy][sx] = True
    q = deque()
    q.append([sy, sx, 0])
    canEat = False
    fy, fx = 1e9, 1e9
    stopTime = 1e9
    while q:
        y, x, t = q.popleft()
        if stopTime < t:
            break
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and n > tmpX >= 0 and \
                  not visit[tmpY][tmpX] and sharksize >= grid[tmpY][tmpX]:
                if grid[tmpY][tmpX] == 0 or grid[tmpY][tmpX] == sharksize:
                    visit[tmpY][tmpX] = True
                    q.append([tmpY, tmpX, t + 1])
                else:
                    if stopTime >= t + 1:
                        stopTime = t + 1
                        if fy > tmpY or fy == tmpY and fx > tmpX:
                            fy, fx = tmpY, tmpX
    if fy != 1e9:
        time += stopTime
        cnt += 1
        canEat = True
        grid[fy][fx] = 0
        sy, sx = fy, fx
print(time)

# https://www.acmicpc.net/problem/16236