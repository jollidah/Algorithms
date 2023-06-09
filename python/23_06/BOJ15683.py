# 감시

import sys

# def printGrid():
#     for y in range(n):
#         print(*grid_cnt[y])
#     print()

def update_grid(y, x, dy, dx):
    tmpY = y + dy
    tmpX = x + dx
    cnt = 0
    while n > tmpY >= 0 and m > tmpX >= 0 and grid[tmpY][tmpX] != 6:
        if grid_cnt[tmpY][tmpX] == 0 : cnt += 1
        grid_cnt[tmpY][tmpX] += 1
        tmpY += dy
        tmpX += dx
    return cnt

def rollback(y, x, dy, dx):
    tmpY = y + dy
    tmpX = x + dx
    while n > tmpY >= 0 and m > tmpX >= 0 and grid[tmpY][tmpX] != 6:
        grid_cnt[tmpY][tmpX] -= 1
        tmpY += dy
        tmpX += dx

def DFS(idx, cnt):
    if cnt == 0:
        print(0)
        exit(0)
    if idx == len(candidates):
        return cnt
    y, x, c_num = candidates[idx]

    minV = 100
    for d in range(turn_avil[c_num]):
        tmpC = 0
        for tmpDy, tmpDx in cctv[c_num]:
            dy, dx = tmpDy, tmpDx
            for _ in range(d):
                dy = - tmpDx
                dx = tmpDy
                tmpDy = dy
                tmpDx = dx
            tmpC += update_grid(y, x, dy, dx)
        minV = min(minV, DFS(idx + 1, cnt - tmpC))
        for tmpDy, tmpDx in cctv[c_num]:
            dy, dx = tmpDy, tmpDx
            for _ in range(d):
                dy = - tmpDx
                dx = tmpDy
                tmpDy = dy
                tmpDx = dx
            rollback(y, x, dy, dx)
    return minV


inp = sys.stdin.readline
n, m = map(int, inp().split())
grid = [list(map(int, inp().split())) for _ in range(n)]
grid_cnt = [[0 for _ in range(m)] for _ in range(n)]
turn_avil = [0, 4, 2, 4, 4]
candidates = []
cctv_5 = []
tmpC = 0
cctv = [
    [],
    [[0, 1]],
    [[0, -1], [0, 1]],
    [[1, 0], [0, 1]],
    [[0, -1], [1, 0], [0, 1]]
]

for y in range(n):
    for x in range(m):
        if grid[y][x] == 0:
            tmpC += 1
        else:
            grid_cnt[y][x] += 1
            if 5 > grid[y][x] > 0:  
                candidates.append([y, x, grid[y][x]])
            if grid[y][x] == 5:
                cctv_5.append([y, x])

for y, x in cctv_5:
    tmpC -= update_grid(y, x, 0, 1)
    tmpC -= update_grid(y, x, 1, 0)
    tmpC -= update_grid(y, x, 0, -1)
    tmpC -= update_grid(y, x, -1, 0)

print(DFS(0, tmpC))

# https://www.acmicpc.net/problem/15683