# 알고스팟

import sys
from queue import PriorityQueue

inp = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
m, n = map(int, inp().split())
grid = [inp().strip() for _ in range(n)]
dp = [[1e9 for _ in range(m)] for _ in range(n)]
q = PriorityQueue()
minV = 1e9

q.put([0, 0, 0])

while not q.empty():
    cnt, y, x = q.get()
    if y == n - 1 and x == m - 1:
        print(cnt)
        break
    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        tmpC = cnt
        if n > tmpY >= 0 and m > tmpX >= 0:
            if grid[tmpY][tmpX] == "1":
                tmpC += 1
            if dp[tmpY][tmpX] > tmpC:
                dp[tmpY][tmpX] = tmpC
                q.put([tmpC, tmpY, tmpX])
        
# https://www.acmicpc.net/problem/1261