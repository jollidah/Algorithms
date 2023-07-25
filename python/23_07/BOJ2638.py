# 치즈

import sys
from collections import deque

def update_air(y, x):
    q = deque()
    q.append([y, x])
    air[y][x] = True
    while q:
        y, x = q.popleft()
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0\
                and grid[tmpY][tmpX] == 0 and not air[tmpY][tmpX]:
                air[tmpY][tmpX] = True
                q.append([tmpY, tmpX])

inp = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

n, m = map(int, inp().split())
cnt = 0
cheeses = []
air = [[False for _ in range(m)] for _ in range(n)]
grid = [list(map(int, inp().split())) for _ in range(n)]

for y in range(n):
    for x in range(m):
        if grid[y][x] == 1:
            cheeses.append([y, x])

update_air(0, 0)

while cheeses:
    cnt += 1
    remove = []
    for i in range(len(cheeses) - 1, -1, -1):
        tmpCnt = 0
        y, x = cheeses[i]
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0 and air[tmpY][tmpX]:
                tmpCnt += 1
        if tmpCnt >= 2:
            remove.append(i)
    for i in remove:
        y, x = cheeses[i]
        grid[y][x] = 0
        update_air(y, x)
        cheeses.pop(i)
print(cnt)

# https://www.acmicpc.net/problem/2638