# 봄버맨

import sys

def putBomb(idx):
    if idx % 4 == 3:
        bomb = 1
    else:
        bomb = -1
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 0:
                grid[y][x] = bomb

def bomb(idx):
    if idx % 4 == 2:
        bomb = 1
    else:
        bomb = -1
    for y in range(r):
        for x in range(c):
            if grid[y][x] == bomb:
                isBomb[y][x] = True
                for d in range(4):
                    tmpY = y + dy[d]
                    tmpX = x + dx[d]
                    if r > tmpY >= 0 and c > tmpX >= 0:
                        isBomb[tmpY][tmpX] = True
    for y in range(r):
        for x in range(c):
            if isBomb[y][x]:
                grid[y][x] = 0

inp = sys.stdin.readline
r, c, n = map(int, inp().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
grid = []
for y in range(r):
    inputString = inp().strip()
    tmp = []
    for x in range(c):
        if inputString[x] == ".":
            tmp.append(0)
        else:
            tmp.append(1)
    grid.append(tmp)

cnt = 0
for i in range(1, n):
    if i % 2 == 1:
        putBomb(i)
    else:
        isBomb = [[False for _ in range(c)] for _ in range(r)]
        bomb(i)
            
for y in range(r):
    for x in range(c):
        print("." if grid[y][x] == 0 else "O", end = "")
    print()

# https://www.acmicpc.net/problem/16918