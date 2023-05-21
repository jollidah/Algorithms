# 택배

import sys
from collections import deque

inp = sys.stdin.readline
n, m = map(int, inp().split())
vertexes = [[] for _ in range(n + 1)]
res = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, inp().split())
    vertexes[a].append([b, c])
    vertexes[b].append([a, c])

for i in range(1, n + 1):
    q = deque()
    dp = [1e7 for _ in range(n + 1)]
    dp[i] = 0
    q.append([0, i])
    while q:
        c, p = q.popleft()
        for child, cost in vertexes[p]:
            if dp[child] > c + cost:
                dp[child] = c + cost
                res[child][i] = p
                q.append([c + cost, child])
for y in range(1, n + 1):
    for x in range(1, n + 1):
        if y == x:
            print("-", end = " ")
        else:
            print(res[y][x], end = " ")
    print()

# https://www.acmicpc.net/problem/1719