# 서울 지하철 2호선

import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input().strip())
childs = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]
res = [0 for _ in range(n + 1)]

cycle = set()

def DFS(ex, i):
    if visit[i]:
        for t in range(len(tmp)):
            if tmp[t] == i:
                for j in tmp[t:]:
                    cycle.add(j)
    else:
        visit[i] = True
        tmp.append(i)
        for child in childs[i]:
            if child != ex:
                DFS(i, child)
        tmp.pop()

# 그래프 업데이트
for _ in range(n):
    a, b = map(int, input().split())
    childs[a].append(b)
    childs[b].append(a)

# Cycle detection
for i in range(1, n + 1):
    if not visit[i]:
        tmp = []
        DFS(0, i)

visit = [False for _ in range(n + 1)]
q = deque()
for node in cycle:
    q.append([0, node])
    visit[node] = True

# BFS를 활용한 다익스트라
while q:
    cnt, node = q.popleft()
    for child in childs[node]:
        if not visit[child]:
            visit[child] = True
            res[child] = cnt + 1
            q.append([cnt + 1, child])
print(*res[1:])

# https://www.acmicpc.net/problem/16947