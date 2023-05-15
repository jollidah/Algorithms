# 가장 긴 증가하는 부분 수열 5

import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline
n = int(input().strip())
nList = list(map(int, input().split()))
lis = [nList[0]]
lisIdx = [[0]]
dp = [i for i in range(n)]

for i in range(1, n):
    if lis[-1] < nList[i]:
        dp[i] = lisIdx[-1][-1]
        lis.append(nList[i])
        lisIdx.append([i])
        
    else:
        k = bisect_left(lis, nList[i])
        if k != 0:
            dp[i] = lisIdx[k - 1][-1]
        lisIdx[k].append(i)
        lis[k] = nList[i]

idx = lisIdx[-1][0]
res = [nList[idx]]

while idx != dp[idx]:
    idx = dp[idx]
    res.append(nList[idx])

print(len(lis))
for i in range(len(lis) - 1, -1, -1):
    print(res[i], end = " ")

# https://www.acmicpc.net/problem/14003