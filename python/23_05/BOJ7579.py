# 앱

import sys

inp = sys.stdin.readline
n, m = map(int, inp().split())
mList = list(map(int, inp().split()))
cList = list(map(int, inp().split()))
tc = sum(cList) + 1
dp = [[0 for _ in range(tc)] for _ in range(n + 1)]

res = int(1e9)
for i in range(n):
    for t in range(cList[i]):
        dp[i + 1][t] = dp[i][t]
    for t in range(cList[i], tc):
        dp[i + 1][t] = max(dp[i][t], dp[i][t - cList[i]] + mList[i])
        if dp[i + 1][t] >= m:
            res = min(res, t)
print(res)

# https://www.acmicpc.net/problem/7579