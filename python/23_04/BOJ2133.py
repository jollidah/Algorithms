# 타일 채우기

import sys

input = sys.stdin.readline
n = int(input().strip())
if n == 0:
    print(0)
    exit(0)
dp = [1, 0, 3, 0] + [0 for _ in range(n - 3)]

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * 3
    for t in range(i - 4, -1, -2):
        dp[i] += dp[t] * 2

print(dp[n])

# https://www.acmicpc.net/problem/2133