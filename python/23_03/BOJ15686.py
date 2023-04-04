# 치킨 배달

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
dp = [[[] for _ in range(n)] for __ in range(n)]
house_mean = [0, 0]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dq = deque()
cnt = 0

for y in range(n):
    for x in range(n):
        if grid[y][x] == 1:
            house.append([y, x])
        elif grid[y][x] == 2:
            chicken.append([y, x])
            dq.append([y, x, cnt, 0])
            dp[y][x].append([cnt, 0])
            cnt += 1

visited = [[[False for _ in range(n)] for __ in range(n)] for ___ in range(len(chicken))]
for i in range(len(chicken)):
    visited[i][chicken[i][0]][chicken[i][1]] = True

while dq:
    y, x, cnt, dist = dq.popleft()
    for i in range(4):
        tmpY = y + dy[i]
        tmpX = x + dx[i]
        if n > tmpY >= 0 and n > tmpX >= 0 and not visited[cnt][tmpY][tmpX]:
            visited[cnt][tmpY][tmpX] = True    
            dp[tmpY][tmpX].append([cnt, dist + 1])
            dq.append([tmpY, tmpX, cnt, dist + 1])

house_mean = [sum(x[0] for x in house) / len(house), sum(x[1] for x in house) / len(house)]
res = 1e9
resPos = []
for comb in combinations(range(len(chicken)), m):
    tmpRes = 0
    for y, x in house:
        for chicken_num, dist in dp[y][x]:
            if chicken_num in comb:
                tmpRes += dist
                break
    res = min(res, tmpRes)

print(res)

# https://www.acmicpc.net/problem/15686