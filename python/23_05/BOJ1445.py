# 일요일 아침의 데이트

import sys
from queue import PriorityQueue

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
inp = sys.stdin.readline
h, w = map(int, inp().split())
tg = [[False for _ in range(w)] for _ in range(h)]
t = set()
target = [0, 0]
start = [0, 0]

for y in range(h):
    tmp = inp().strip()
    for x in range(w):
        if tmp[x] == "F":
            target = [y, x]
        elif tmp[x] == "g":
            t.add((y, x))
        elif tmp[x] == "S":
            start = [y, x]

for y, x in t:
    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        if h > tmpY >= 0 and w > tmpX >= 0:
            tg[tmpY][tmpX] = True

visited = [[False for _ in range(w)] for _ in range(h)]
q = PriorityQueue()
visited[start[0]][start[1]] = True
q.put([0, 0, start[0], start[1]])

while not q.empty():
    tn, gn, py, px = q.get()
    for d in range(4):
        tmpY = py + dy[d]
        tmpX = px + dx[d]
        if h > tmpY >= 0 and w > tmpX >= 0 and not visited[tmpY][tmpX]:
            visited[tmpY][tmpX] = True
            if [tmpY, tmpX] == target:
                print(tn, gn)
                exit(0)
            if (tmpY, tmpX) in t:
                q.put([tn + 1, gn, tmpY, tmpX])
            elif tg[tmpY][tmpX]:
                q.put([tn, gn + 1, tmpY, tmpX])
            else:
                q.put([tn, gn, tmpY, tmpX])

# https://www.acmicpc.net/problem/1445