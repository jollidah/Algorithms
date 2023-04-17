# 내리막 길

import sys

def DFS(y, x):
    if y == n - 1 and x == m - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    res = 0
    for p in range(4):
        tmpY = y + dy[p]
        tmpX = x + dx[p]
        if n > tmpY >= 0 and m > tmpX >= 0 and \
            not visit[tmpY][tmpX] and grid[y][x] > grid[tmpY][tmpX]:
            visit[tmpY][tmpX] = True
            res += DFS(tmpY, tmpX)
            visit[tmpY][tmpX] = False
    dp[y][x] = res
    return res

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for __ in range(m)] for _ in range(n)]
dp = [[-1 for __ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print(DFS(0,0))

# https://www.acmicpc.net/problem/1520