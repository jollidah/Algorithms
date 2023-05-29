# 중량제한

import sys
from queue import PriorityQueue

inp = sys.stdin.readline
n, m = map(int, inp().split())
wList = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, inp().split())
    wList[a].append([b, c])
    wList[b].append([a, c])

s, e = map(int, inp().split())
q = PriorityQueue()
q.put([int(-1e9), s])

while q:
    recentW, p = q.get()
    if visit[p]:
        continue
    if p == e:
        print(-recentW)
        break
    visit[p] = True
    for next, nextW in wList[p]:
        w = min(-recentW, nextW)
        q.put([-w, next])
        
# https://www.acmicpc.net/problem/1939