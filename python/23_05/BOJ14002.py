# 가장 긴 증가하는 부분 수열 4

import sys

input = sys.stdin.readline

n = int(input().strip())
nList = list(map(int, input().split()))

dp = [[1, i] for i in range(n)]
res = []
for i in range(n):
    for t in range(i):
        if nList[t] < nList[i]:
            if dp[i][0] <= dp[t][0]:
                dp[i] = [dp[t][0] + 1, t]
maxCnt = 0
idx = 0
for i in range(n):
    if dp[i][0] > maxCnt:
        maxCnt = dp[i][0]
        idx = i
print(maxCnt)
while idx != dp[idx][1]:
    res.append(nList[idx])
    idx = dp[idx][1]
res.append(nList[idx])
print(*res[::-1])

# https://www.acmicpc.net/problem/14002