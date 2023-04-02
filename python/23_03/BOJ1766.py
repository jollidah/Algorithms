# 문제집

import sys
from queue import PriorityQueue

n, m = map(int, sys.stdin.readline().split())
indegree = [0 for _ in range(n + 1)]
childs = [[] for _ in range(n + 1)]
res = []
s = set(range(1, n + 1))
pq = PriorityQueue()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    indegree[b] += 1
    childs[a].append(b)
    if b in s:
        s.remove(b)

for n in s:
    pq.put(n)

while not pq.empty():
    n = pq.get()
    res.append(n)
    for child in childs[n]:
        if indegree[child] == 1:
            pq.put(child)
        else:
            indegree[child] -= 1

print(*res)

# https://www.acmicpc.net/problem/1766