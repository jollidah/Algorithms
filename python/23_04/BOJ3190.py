# 뱀

import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
apple = [[False for _ in range(n + 2)] for __ in range(n + 2)]
wall = [[False for _ in range(n + 2)] for __ in range(n + 2)]
snake = deque()
inputL = []
for y in [0, n + 1]:
    for x in range(n + 2):
        wall[y][x] = True

for y in range(n + 2):
    for x in [0, n + 1]:
        wall[y][x] = True

for _ in range(int(input().strip())):
    y, x = map(int, input().split())
    apple[y][x] = True

ex = 0
for _ in range(int(input().strip())):
    x, c = input().split()
    inputL.append([int(x) - ex, c])
    ex = int(x)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
hy, hx, ty, tx = 1, 1, 1, 1
d = 1
wall[1][1] = True
snake.append([1, 1])
cnt = 0
    
for x, c in inputL:
    for __ in range(int(x)):
        cnt += 1
        hy += dy[d]
        hx += dx[d]
        if not apple[hy][hx]:
            wall[ty][tx] = False
            ty, tx = snake.popleft()
        else:
            apple[hy][hx] = False
        if wall[hy][hx]:
            print(cnt)
            exit(0)
        snake.append([hy, hx])
        wall[hy][hx] = True
    if c == "L":
        d = (d + 3) % 4
    else:
        d = (d + 1) % 4
while True:
    cnt += 1
    hy += dy[d]
    hx += dx[d]
    if wall[hy][hx]:
        print(cnt)
        exit(0)

# https://www.acmicpc.net/problem/3190