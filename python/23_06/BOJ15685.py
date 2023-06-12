# 드래곤 커브

import sys

def make_dp(idx):
    while idx + 1 != len(dp):
        dp.append(dp[-1] + [(direction + 1) % 4 for direction in dp[-1][-1::-1]])

def make_dragon(targetY, targetX, d, idx):
    if len(dp) <= idx:
        make_dp(idx)
    grid[targetY][targetX] = 1
    for direction in dp[idx]:
        direction = (direction + d) % 4
        targetY += dy[direction]
        targetX += dx[direction]
        grid[targetY][targetX] = 1

inp = sys.stdin.readline
n = int(inp().strip())
dp = [[0]]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
grid = [[False for _ in range(101)] for _ in range(101)]
for _ in range(n):
    x, y, d, g = map(int, inp().split())
    make_dragon(y, x, d , g)

res = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1]:
            res += 1
print(res)

# https://www.acmicpc.net/problem/15685