# 빙산

import sys
from collections import deque

def check(inputY, inputX, s):
    visit = [[False for _ in range(m)] for __ in range(n)]
    q = deque()
    visit[inputY][inputX] = True
    q.append([inputY, inputX])
    ts = 0
    while q:
        y, x = q.popleft()
        ts += 1
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if (tmpY, tmpX) in candidates and not visit[tmpY][tmpX]:
                visit[tmpY][tmpX] = True
                q.append([tmpY, tmpX])
    return ts == s

input = sys.stdin.readline
n , m = map(int, input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
candidates = set()
grid = []
dc = [[0 for _ in range(m)] for __ in range(n)]

for y in range(n):
    grid.append(list(map(int, input().split())))
    for x in range(m):
        if grid[y][x] != 0:
            candidates.add((y, x))
        else:
            for d in range(4):
                tmpY = y + dy[d]
                tmpX = x + dx[d]
                if n  > tmpY >= 0 and m > tmpX >= 0:
                    dc[tmpY][tmpX] += 1
isOkay = True
cnt = 0
while isOkay:
    zeros = []
    rList = []
    for y, x in candidates:
        grid[y][x] = max(grid[y][x] - dc[y][x], 0)
        if grid[y][x] == 0:
            zeros.append([y, x])
    for y, x in zeros:
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            dc[tmpY][tmpX] += 1
        candidates.remove((y, x))
    cnt += 1
    if len(candidates) == 0:
        cnt = 0
        break
    y, x = candidates.pop()
    isOkay = check(y, x, len(candidates) + 1)
    candidates.add((y, x))
print(cnt)
        
# https://www.acmicpc.net/problem/2573