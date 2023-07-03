# 불!

import sys
from collections import deque

def update_fire():
    global fires
    tmp = []
    while fires:
        y, x = fires.pop()
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if r > tmpY >= 0 and c > tmpX >=0 \
                and not wall[tmpY][tmpX]:
                tmp.append([tmpY, tmpX])
                wall[tmpY][tmpX] = True
    fires = tmp

inp = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
r, c = map(int, inp().split())
wall = [[False for _ in range(c)] for _ in range(r)]
visit = [[False for _ in range(c)] for _ in range(r)]
fires = []
q = deque()

for y in range(r):
    tmp = inp().rstrip()
    for x in range(c):
        if tmp[x] == "#":
            wall[y][x] = True
        elif tmp[x] == "J":
            q.append([y, x, 0])
        elif tmp[x] == "F":
            fires.append([y, x])
            wall[y][x] = True

ex = 0
while q:
    y, x, cnt = q.popleft()
    if cnt != ex:
        ex = cnt
        update_fire()
    if wall[y][x] or visit[y][x]:
        continue
    if y == 0 or y == r - 1 or x == 0 or x == c - 1:
        print(cnt + 1)
        break
    # 스테이지 업
    visit[y][x] = True
    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        if r > tmpY >= 0 and c > tmpX >=0 \
            and not wall[tmpY][tmpX]:
            q.append([tmpY, tmpX, cnt + 1])
else:
    print("IMPOSSIBLE")

# https://www.acmicpc.net/problem/4179