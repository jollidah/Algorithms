# 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS():
    dq = deque()
    dq.append([0, 0, 0, 1])
    while dq:
        y, x, bc, cnt = dq.popleft()
        if y == n - 1 and x == m -1:
            return cnt
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0:
                if toVisit[tmpY][tmpX][bc]:
                    toVisit[tmpY][tmpX][bc] = False
                    if isWall[tmpY][tmpX] and bc == 0:
                        dq.append([tmpY, tmpX, bc + 1, cnt + 1])
                    elif not isWall[tmpY][tmpX]:
                        dq.append([tmpY, tmpX, bc, cnt + 1])
    return -1

n, m = map(int, input().split())
toVisit = [[[True, True] for _ in range(m)] for __ in range(n)]
isWall = []
toVisit[0][0] = [False, False]
for _ in range(n):
    isWall.append(list(map(lambda x: True if x == "1" else False, [s for s in input().strip()])))
print(BFS())

# https://www.acmicpc.net/problem/2206