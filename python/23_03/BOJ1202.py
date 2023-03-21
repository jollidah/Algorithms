# 토마토

import sys
from queue import Queue

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

q = Queue()
w, h = map(int, sys.stdin.readline().split())
grid = []
toVisit = [[True for i in range(w)] for t in range(h)]
cnt = w * h
day = 0

for _ in range(h):
    grid.append(list(map(int, sys.stdin.readline().split())))
for i in range(h):
    for t in range(w):
        if grid[i][t] != 0:
            if grid[i][t] == 1:
                q.put([i, t, day])
            toVisit[i][t] = False
            cnt -= 1


while not q.empty():
    y, x, day = q.get()
    for i in range(4):
        tmpY = y + dy[i]
        tmpX = x + dx[i]
        if(h > tmpY >= 0 and w > tmpX >= 0 and toVisit[tmpY][tmpX]):
            toVisit[tmpY][tmpX] = False
            q.put([tmpY, tmpX, day + 1])
            cnt -= 1
print(day if cnt == 0 else -1)

# https://www.acmicpc.net/problem/7576