# 특정한 최단 경로

import sys
from collections import deque

def BFS(start, end) -> int:
    dq = deque()
    dq.append([start, 0])
    dp = [1e9 for _ in range(n + 1)]
    dp[start] = 0
    res = 1e9
    while dq:
        s, c = dq.popleft()
        if s == end:
            res = min(res, c)
            continue
        for child, cost in childs[s]:
            if dp[child] > c + cost:
                dp[child] = c + cost
                dq.append([child, c + cost])
    if res == 1e9:
        print(-1)
        exit(0)
    return res

input = sys.stdin.readline
n, e = map(int, input().split())
childs = [[]for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    childs[a].append([b, c])
    childs[b].append([a, c])
t1, t2 = map(int, input().split())

a1 = BFS(1, t1)
a2 = BFS(1, t2)
b = BFS(t1, t2)
c1 = BFS(t1, n)
c2 = BFS(t2, n)
res = min(a1 + c2 + b, a2 + c1 + b)

print(res)

# https://www.acmicpc.net/problem/1504