# 외판원 순회 3

import sys
import math

def DFS(p, path):
    if dp[p][path] != 1e9:
        return dp[p][path]
    if path == (1 << n) - 1:
        return cost[p][0]
    
    for i in range(n):
        if path & 1 << i != 0:
            continue
        dp[p][path] = min(dp[p][path], cost[p][i] + DFS(i, path | 1 << i))
    return dp[p][path]

input = sys.stdin.readline
n = int(input().strip())
pList = [list(map(int, input().split())) for _ in range(n)]
cost = [[0 for _ in range(n)] for _ in range(n)]
dp = [[1e9 for _ in range(1 << n)] for _ in range(n)]

for i in range(n):
    for t in range(i):
        cost[i][t] = cost[t][i] = math.sqrt(pow(pList[i][0] - pList[t][0], 2) + pow(pList[i][1] - pList[t][1], 2))

print(DFS(0, 0))

# https://www.acmicpc.net/problem/16991