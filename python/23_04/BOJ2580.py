# 스도쿠

import sys
from collections import deque

def rowCheck(y, x, n):
    return n not in grid[y]

def columnCheck(y, x, n):
    for t in range(9):
        if n == grid[t][x]:
            return False
    return True

def boxCheck(y, x, n):
    tmpY = (y // 3) * 3
    tmpX = (x // 3) * 3
    for i in range(3):
        for t in range(3):
            if n == grid[tmpY + i][tmpX + t]:
                return False
    return True

def DFS():
    if not zeros:
        for l in grid:
            print(*l)
        exit(0)
    else:
        y, x = zeros.popleft()
        for n in range(1, 10):
            if rowCheck(y, x, n) and columnCheck(y, x, n) and boxCheck(y, x, n):
                grid[y][x] = n
                DFS()
                grid[y][x] = 0
        zeros.appendleft([y, x])


grid = []
rows = [set(range(1, 10)) for _ in range(9)]
columns = [set(range(1, 10)) for _ in range(9)]
boxes = [[set(range(1, 10)) for _ in range(3)] for __ in range(3)]
zeros = deque()
for y in range(9):
    grid.append(list(map(int, sys.stdin.readline().split())))
    for x in range(9):
        if grid[y][x] == 0:
            zeros.append([y, x])
DFS()

# https://www.acmicpc.net/problem/2580