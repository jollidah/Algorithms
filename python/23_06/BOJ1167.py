# 트리의 지름

import sys
from collections import deque

def BFS(p):
    q = deque()
    q.append([0, p])
    dp = [0 for _ in range(v + 1)]
    dp[p] = -1
    maxV = 0
    maxIdx = 0
    while q:
        cost, node = q.popleft()
        for next, c in tree[node]:
            if not dp[next]:
                dp[next] = cost + c
                if cost + c > maxV:
                    maxV = cost + c
                    maxIdx = next
                q.append([dp[next], next])
    return [maxIdx, maxV]

inp = sys.stdin.readline

v = int(inp().rstrip())
tree = [[] for _ in range(v + 1)]
candidate = 0
for t in range(1, v + 1):
    tmp = list(map(int, inp().split()))
    if len(tmp) == 4:
        candidate = t
    for i in range(1, len(tmp) - 1, 2):
        tree[tmp[0]].append([tmp[i], tmp[i + 1]])

print(BFS(BFS(candidate)[0])[1])

# https://www.acmicpc.net/problem/1167