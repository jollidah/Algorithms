# 게임 개발

import sys
from collections import deque

def Solution():
    inp = sys.stdin.readline
    n = int(inp())
    res = [0 for _ in range(n)]
    cost = []
    indegree = [0 for _ in range(n)]
    next_node = [[] for _ in range(n)]
    q = deque()

    for i in range(n):
        tmp = list(map(int, inp().split()))
        if len(tmp) == 2:
            q.append([i, tmp[0]])
            res[i] = tmp[0]
            for t in range(1, len(tmp) - 1):
                indegree[tmp[t] - 1] -= 1
        cost.append(tmp[0])
        indegree[i] += len(tmp) - 2
        for t in range(1, len(tmp) - 1):
            next_node[tmp[t] - 1].append(i)

    while q:
        node, c = q.popleft()
        for next in next_node[node]:
            res[next] = max(res[next], c + cost[next])
            if indegree[next] == 1:
                q.append([next, res[next]])
            else:
                indegree[next] -= 1
    return res

if __name__ == "__main__":
    for num in Solution():
        print(num, end = "\n")

# https://www.acmicpc.net/problem/1516