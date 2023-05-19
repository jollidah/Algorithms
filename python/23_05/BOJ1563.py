# 개근상

import sys

inp = sys.stdin.readline

MOD = 1000000
n = int(input())
dp = [[[0 for _ in range(3)] for _ in range(2)]
      for _ in range(n+1)]  # i, 지각, 결석
dp[1][0][0] = dp[1][1][0] = dp[1][0][1] = 1
for i in range(2, n+1):
    dp[i][0][0] = sum(dp[i-1][0]) % MOD
    dp[i][1][0] = sum(dp[i-1][0]) % MOD + sum(dp[i-1][1]) % MOD
    dp[i][0][1] = dp[i-1][0][0] % MOD
    dp[i][1][1] = dp[i-1][1][0] % MOD
    dp[i][0][2] = dp[i-1][0][1] % MOD
    dp[i][1][2] = dp[i-1][1][1] % MOD

print((sum(dp[n][0]) + sum(dp[n][1])) % MOD)

# https://www.acmicpc.net/problem/1563