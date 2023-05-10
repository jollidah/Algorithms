# 가장 긴 증가하는 부분 순열

import sys

input = sys.stdin.readline

n = int(input().strip())
nList = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nList[j] < nList[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# https://www.acmicpc.net/problem/11053