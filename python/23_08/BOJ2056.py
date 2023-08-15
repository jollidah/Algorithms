# 직업

import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    n = int(inp())
    if n == 0:
        print(0)
        exit(0)
    dp = [0 for _ in range(n + 1)]
    indegree = [0]
    cost = [0]
    childs = [[] for _ in range(n + 1)]
    candidates = []

    for i in range(1, n + 1):
        tmp = list(map(int, inp().split()))
        cost.append(tmp[0])
        if tmp[1] == 0:
            candidates.append(i)
        indegree.append(tmp[1])
        for node in range(2, len(tmp)):
            childs[tmp[node]].append(i)
    q = deque()
    for candidate in candidates:
        q.append([candidate, cost[candidate]])
        dp[candidate] = cost[candidate]
    while q:
        node, c = q.popleft()
        for child in childs[node]:
            dp[child] = max(dp[child], c + cost[child])
            if indegree[child] == 1:
                q.append((child, dp[child]))
            else:
                indegree[child] -= 1
    return max(dp)

if __name__ == "__main__":
    print(solution())

# https://www.acmicpc.net/problem/2056