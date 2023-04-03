# 최단경로

import sys
from queue import PriorityQueue

v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())
edges = [{} for _ in range(v + 1)]
dp = [-1 for _ in range(v + 1)]
pq = PriorityQueue()

for _ in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    if b in edges[a].keys():
        edges[a][b] = min(edges[a][b], w)
    else:
        edges[a][b] = w

pq.put([0, start])

while not pq.empty():
    c, p = pq.get()
    if dp[p] == -1:
        dp[p] = c
        for edge, cost in edges[p].items():
            pq.put([c + cost, edge])
    # print(c, p)


for n in dp[1:]:
    print(n if n != -1 else "INF")

# https://www.acmicpc.net/problem/1753