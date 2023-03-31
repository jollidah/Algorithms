# 줄 세우기

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
res = []
s = set(range(1, n + 1))
dq = deque()

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    if b in s:
        s.remove(b)

# indegree가 0인 것들 append
for n in s:
    dq.append(n)

while dq:
    n = dq.popleft()
    res.append(n)
    for child in graph[n]:
        if indegree[child] == 1:
            dq.append(child)
        else:
            indegree[child] -= 1

print(*res)

# https://www.acmicpc.net/problem/2252