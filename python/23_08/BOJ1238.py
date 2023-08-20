# 파티

import sys
from collections import deque

def solution():
    inp = sys.stdin.readline

    n, m, x = map(int, inp().split())
    flist = [[] for _ in range(n + 1)]
    tlist = [[] for _ in range(n + 1)]
    fdp = [1e9] * (n + 1)
    tdp = [1e9] * (n + 1) 
    fdp[x], tdp[x] = 0, 0

    for _ in range(m):
        f, t, c = map(int, inp().split())
        flist[f].append((t, c))
        tlist[t].append((f, c))

    q = deque()
    q.append((x, 0))
    while q:
        pos, cost = q.popleft()
        for next, c in flist[pos]:
            if fdp[next] > cost + c:
                fdp[next] = cost + c
                q.append((next, fdp[next]))

    q.append((x, 0))
    while q:
        pos, cost = q.popleft()
        for next, c in tlist[pos]:
            if tdp[next] > cost + c:
                tdp[next] = cost + c
                q.append((next, tdp[next]))

    maxV = 0
    for i in range(1, n + 1):
        maxV = max(maxV, fdp[i] + tdp[i])
    return maxV

if __name__ == "__main__":
    print(solution())

# https://www.acmicpc.net/problem/1238