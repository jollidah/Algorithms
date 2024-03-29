# 외판원 순회

import sys

def DFS(p, path):
    if dp[p][path] != 1e9:
        return dp[p][path]
    
    if path == (1 << (n - 1)) - 1:
        if cost[p][0]:
            return cost[p][0]
        else:
            return 1e9
        
    for i in range(1, n):
        if not cost[p][i]:
            continue
        if path & (1 << i - 1):
            continue
        dp[p][path] = min(dp[p][path], cost[p][i] + DFS(i, path | (1 << (i - 1))))
    return dp[p][path]


input = sys.stdin.readline
n = int(input().strip())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e9 for _ in range(1 << n)] for _ in range(n)]
# dp[p][path] -> i에서 path에 들어 있는 점들을 지나 0으로 향하는 최소비용

print(DFS(0, 0))

# https://www.acmicpc.net/problem/2098