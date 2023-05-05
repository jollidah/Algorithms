# 말이 되고픈 원숭이

import sys
from collections import deque

input = sys.stdin.readline

k = int(input().strip())
w, h = map(int, input().split())
if w == 1 and h == 1:
    print(0)
    exit(0)

isWall = [[False for _ in range(w)] for __ in range(h)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

hdy = [1, 2, 2, 1, -1, -2, -2, -1]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
dp = [[[True for _ in range(k + 1)] for _ in range(w)] for _ in range(h)]
for y in range(h):
    tmp = list(map(int, input().split()))
    for x in range(w):
        if tmp[x] == 1:
            isWall[y][x] = True

q = deque()
q.append([0, 0, k, 0])

while q:
    y, x, cnt, path = q.popleft()
    if cnt != 0:
        for d in range(8):
            tmpY = y + hdy[d]
            tmpX = x + hdx[d]
            if h > tmpY >= 0 and w > tmpX >= 0 and \
                dp[tmpY][tmpX][cnt - 1] and not isWall[tmpY][tmpX]:
                if tmpY == h - 1 and tmpX == w - 1:
                    print(path + 1)
                    exit(0)
                dp[tmpY][tmpX][cnt - 1] = False
                q.append([tmpY, tmpX, cnt - 1, path + 1])

    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        if h > tmpY >= 0 and w > tmpX >= 0 and \
            dp[tmpY][tmpX][cnt] and not isWall[tmpY][tmpX]:
            if tmpY == h - 1 and tmpX == w - 1:
                print(path + 1)
                exit(0)
            dp[tmpY][tmpX][cnt] = False
            q.append([tmpY, tmpX, cnt, path + 1])
print(-1)

# https://www.acmicpc.net/problem/1600