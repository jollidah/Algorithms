# 평범한 배낭

import sys

inp = sys.stdin.readline

n, k = map(int, inp().split())
bags = [list(map(int, inp().split())) for _ in range(n)]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
candidates = [0]

for i in range(n):
    w, v = bags[i]
    tmpCandidate = []
    for candidate in candidates:
        dp[i + 1][candidate] = dp[i][candidate]
    for candidate in candidates:
        if (tmp := candidate + w) <= k:
            if dp[i][tmp] == 0:
                tmpCandidate.append(tmp)
                dp[i + 1][tmp] = dp[i][candidate] + v
            else:
                dp[i + 1][tmp] = max(dp[i][tmp], dp[i][candidate] + v)
    candidates += tmpCandidate
print(max(dp[n]))

# https://www.acmicpc.net/problem/12865