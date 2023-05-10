# 가장 큰 증가하는 부분 순열

import sys
from copy import deepcopy

input = sys.stdin.readline

n = int(input().strip())
nList = list(map(int, input().split()))
dp = deepcopy(nList)

for i in range(n):
    for j in range(i):
        if nList[j] < nList[i]:
            dp[i] = max(dp[j] + nList[i], dp[i])
print(max(dp))

# https://www.acmicpc.net/problem/11055