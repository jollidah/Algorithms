# 이분 그래프

import sys
from collections import deque

input = sys.stdin.readline
for _ in range(int(input().strip())):
    v, e = map(int, input().split())
    edges = [[] for ___ in range(v + 1)]
    vertexes = [0 for ___ in range(v + 1)]
    candidate = set(range(1, v + 1))
    for __ in range(e):
        a, b = map(int , input().split())
        edges[a].append(b)
        edges[b].append(a)
    dq = deque()
    res = True
    while candidate:
        dq.append([candidate.pop(), 1])
        while dq:
            n, col = dq.popleft()
            if vertexes[n] != 0:
                if vertexes[n] != col:
                    res = False
                    candidate.clear()
                    break
                else:
                    continue
            else:
                candidate.discard(n)
                vertexes[n] = col
                for node in edges[n]:
                    dq.append([node, -1 * col])
    print("YES") if res else print("NO")

# https://www.acmicpc.net/problem/1707