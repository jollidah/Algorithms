# 치즈

import sys
from collections import deque

def remove_oxidize():
    for y, x in oxidize_cheeses:
        grid[y][x] = 0

def update_oxidize():
    global oxidize_cheeses
    next = []
    q = deque()
    visit = [[False for _ in range(m)] for _ in range(n)]
    for y, x in oxidize_cheeses:
        visit[y][x] = True
        q.append([y, x])
    while q:
        y, x = q.popleft()
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if m > tmpX >= 0 and n > tmpY >= 0 and not visit[tmpY][tmpX]:
                visit[tmpY][tmpX] = True
                if grid[tmpY][tmpX] == 0:
                    q.append([tmpY, tmpX])
                else:
                    next.append([tmpY, tmpX])
    oxidize_cheeses = next

inp = sys.stdin.readline
cnt = -1
oxidize_cheeses = [[0, 0]]
n, m  = map(int, inp().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
grid = []
remain = 1
for y in range(n):
    grid.append(list(map(int, inp().split())))
    for x in range(m):
        if grid[-1][x] == 1:
            remain += 1

while remain != len(oxidize_cheeses):
    remain -= len(oxidize_cheeses)
    remove_oxidize()
    update_oxidize()
    cnt += 1

print(cnt + 1)
print(remain)

# https://www.acmicpc.net/problem/2636