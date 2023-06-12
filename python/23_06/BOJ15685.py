# 드래곤 커브

import sys

def print_grid():
    for y in range(len(grid)):
        print(*grid[y])

def turn(targetY, targetX, y, x, d):
    y = y - targetY
    x = x - targetX
    for _ in range(d):
        ty = -x
        tx = y
        y, x = ty, tx
    return [targetY + y, targetX + x]

# dp 마지막 요소는 빼고 turn 해야함
def make_dp(idx):
    while idx + 1 != len(dp):
        tmp = []
        targetY , targetX = dp[-1][-1]
        for y, x in dp[-1][-2::-1]:
            tmp.append(turn(targetY, targetX, y, x, 3))
        # print(dp[-1] + tmp)
        dp.append(dp[-1] + tmp)


def make_dragon(targetY, targetX, d, idx):
    if len(dp) <= idx:
        make_dp(idx)
    for y, x in dp[idx]:
        y, x = turn(0, 0, y, x, d)
        grid[targetY + y][targetX + x] = 1


inp = sys.stdin.readline
n = int(inp().strip())
dp = [[[0, 0,], [0, 1]]]
grid = [[0 for _ in range(200)] for _ in range(200)]
for _ in range(n):
    x, y, d, g = map(int, inp().split())
    make_dragon(y, x, d , g)

res = 0
for i in range(200):
    for j in range(200):
        if grid[i][j] == 1 and grid[i + 1][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j + 1] == 1:
            res += 1
print(res)

# https://www.acmicpc.net/problem/15685