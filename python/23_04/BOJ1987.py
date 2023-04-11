# 알파벳

import sys

def BFS():
    q = set([(0, 0, 1, grid[0][0])])
    res = 0
    while q:
        y, x, cnt, s = q.pop()
        res = max(res, cnt)
        for d in range(4):
            tmpY = y + dy[d]
            tmpX = x + dx[d]
            if n > tmpY >= 0 and m > tmpX >= 0 and grid[tmpY][tmpX] not in s:
                    q.add((tmpY, tmpX, cnt + 1, s + grid[tmpY][tmpX]))
    return res

input =sys.stdin.readline
n , m = map(int, input().split())
grid= []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for _ in range(n):
    grid.append(input().strip())
print(BFS())

# https://www.acmicpc.net/problem/1987