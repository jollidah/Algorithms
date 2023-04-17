import sys

input = sys.stdin.readline
n, m = map(int, input().split())
grid= [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(m)] for __ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def plus(y, x):
    t = []
    for p in range(4):
        tmpY = y + dy[p]
        tmpX = x + dx[p]
        if n > tmpY >= 0 and m > tmpX >= 0:
            t.append(grid[tmpY][tmpX])
    if len(t) > 2:
        t.sort()
        return sum(t[-3:]) + grid[y][x]
    return 0

def DFS(y, x, cnt, cost):
    if cnt == 4:
        return cost
    res = 0
    for p in range(4):
        tmpY = y + dy[p]
        tmpX = x + dx[p]
        if n > tmpY >= 0 and m > tmpX >= 0 and not visit[tmpY][tmpX]:
            visit[tmpY][tmpX] = True
            res = max(res, DFS(tmpY, tmpX, cnt + 1, cost + grid[tmpY][tmpX]))
            visit[tmpY][tmpX] = False
    return res

res = 0
for y in range(n):
    for x in range(m):
        visit[y][x] = True
        res = max(res, DFS(y, x, 1, grid[y][x]), plus(y, x))
        visit[y][x] = False
print(res)
