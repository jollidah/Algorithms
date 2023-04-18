# 플로이드

import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
childs =[defaultdict(int) for __ in range(n + 1)]
for __ in range(m):
    a, b, c = map(int, input().split())
    if childs[a][b] != 0:
        c = min(childs[a][b], c)
    childs[a][b] = c
for i in range(1, n + 1):
    q = deque()
    q.append([i, 0])
    dp = [1e9 for _ in range(n + 1)]
    dp[i] = 0
    while q:
        p, c = q.popleft()
        for child in childs[p].keys():
            if dp[child] > c + childs[p][child]:
                dp[child] = c + childs[p][child]
                q.append([child, dp[child]])
    for i in range(1, n + 1):
        print(dp[i] if dp[i] != 1e9 else 0, end= " ")
    print()

# https://www.acmicpc.net/problem/11404