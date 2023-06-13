# 이차원 배열과 연산

import sys
from collections import Counter

inp = sys.stdin.readline

r, c, k = map(int, inp().split())
grid = [list(map(int, inp().split())) for _ in range(3)]

def R():
    maxL = 0
    for i in range(len(grid)):
        tmp = [j for j in grid[i] if j != 0]
        tmp = sorted(Counter(tmp).items(), key = lambda x: (x[1], x[0]))
        grid[i] = []
        for a, b in tmp:
            grid[i].append(a)
            grid[i].append(b)
        maxL = max(maxL, len(grid[i]))
    for i in range(len(grid)):
        while len(grid[i]) != maxL:
            grid[i].append(0)
            grid[i].append(0)


for cnt in range(101):
    try:
        if grid[r - 1][c - 1] == k:
            print(cnt)
            break
    except:
        pass
    if len(grid) >= len(grid[0]):
        R()
    else:
        grid = list(zip(*grid))
        R()
        grid = list(zip(*grid))
else:
    print(-1)

# https://www.acmicpc.net/problem/17140