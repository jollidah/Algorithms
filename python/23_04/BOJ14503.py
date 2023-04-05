# 로봇 청소기

import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
grid = []

n, m = map(int, input().split())
rY, rX, dir = map(int, input().split())
for _ in range(n):
    grid.append(list(map(int, input().split())))
cnt = 0

while True:
    if grid[rY][rX] == 0:
        grid[rY][rX] = 2
        cnt += 1
    clean = True
    for i in range(4):
        tmpY = rY + dy[i]
        tmpX = rX + dx[i]
        if grid[tmpY][tmpX] == 0:
            clean = False
            break
    if clean:
        rY += dy[(dir + 2) % 4]
        rX += dx[(dir + 2) % 4]
        if grid[rY][rX] == 1:
            print(cnt)
            break
    else:
        dir = (dir + 3) % 4
        tmpY = rY + dy[dir]
        tmpX = rX + dx[dir]
        if grid[tmpY][tmpX] == 0:
            rY = tmpY
            rX = tmpX

# https://www.acmicpc.net/problem/14503