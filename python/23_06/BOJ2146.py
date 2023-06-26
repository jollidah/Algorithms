# 다리 만들기

import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp().strip())
grid = []
grounds = []
edges = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for y in range(n):
    grid.append(list(map(int ,inp().split())))
    for x in range(n):
        if grid[-1][x] == 1:
            grounds.append([y, x])
visit = [[False for _ in range(n)] for _ in range(n)]

q = deque()
cnt = -1
for y, x in grounds:
    if not visit[y][x]:
        cnt += 1
        edges.append([])
        q.append([y, x])
        while q:
            y, x = q.popleft()
            edge = False
            for d in range(4):
                tmpY = y + dy[d]
                tmpX = x + dx[d]
                if n > tmpY >= 0 and n > tmpX >= 0:
                    if grid[tmpY][tmpX] == 0:
                        edge = True
                        # edges[cnt].append([y, x])
                    elif not visit[tmpY][tmpX]:
                        visit[tmpY][tmpX] = True
                        q.append([tmpY, tmpX])
            if edge:
                edges[cnt].append([y, x])

res = 1e9
for i in range(len(edges) - 1):
    for j in range(i + 1, len(edges)):
        for y1, x1 in edges[i]:
            for y2, x2 in edges[j]:
                res = min(res, abs(y1 - y2) + abs(x1 - x2))

print(res - 1)

# https://www.acmicpc.net/problem/2146