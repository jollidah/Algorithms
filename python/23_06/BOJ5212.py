# 지구 온난화

import sys

inp = sys.stdin.readline
r,c = map(int, inp().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
maxY, maxX, minY, minX = 0, 0, c, c
grid = []
ground = []
res = [[False for _ in range(c)] for _ in range(r)]
for y in range(r):
    grid.append(inp().strip())
    for x in range(c):
        if grid[-1][x] == "X":
            ground.append([y, x])

for y, x in ground:
    cnt = 0
    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        if c > tmpX >= 0 and r > tmpY >= 0 and grid[tmpY][tmpX] == "X":
            cnt += 1
    if cnt >= 2:
        res[y][x] = True
        minY = min(minY, y)
        minX = min(minX, x)
        maxY = max(maxY, y)
        maxX = max(maxX, x)

for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
        print("X" if res[y][x] else ".", end = "")
    print()

# https://www.acmicpc.net/problem/5212