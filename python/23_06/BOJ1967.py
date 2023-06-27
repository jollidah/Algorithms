# 트리의 지름

import sys
from collections import deque

def dijkstra(s):
    q = deque()
    q.append([s, 0])
    dist[s] = 0
    while q:
        p, d = q.popleft()
        for child, w in tree[p]:
            if dist[child] > d + w:
                dist[child] = d + w
                q.append([child, dist[child]])

def find_max_dist():
    maxV, maxIdx = 0, 0
    for i in range(1, n + 1):
        if dist[i] > maxV:
            maxV = dist[i]
            maxIdx = i
        dist[i] = 1e9
    return [maxIdx, maxV]


inp = sys.stdin.readline
n = int(inp().strip())
if n == 1:
    print(0)
    exit(0)
dist = [1e9 for _ in range(n + 1)]
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, inp().split())
    tree[a].append([b, c])
    tree[b].append([a, c])  


dijkstra(1)
dijkstra(find_max_dist()[0])
print(find_max_dist()[1])

# https://www.acmicpc.net/problem/1967