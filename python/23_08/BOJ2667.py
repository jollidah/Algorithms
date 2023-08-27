# 단지번호붙이기

import sys

from collections import deque

def solution():
    inp = sys.stdin.readline
    dt = ((-1, 0), (1, 0), (0, 1), (0, -1))
    n = int(inp())
    q = deque()
    grid = []
    candidates = set()
    cnt = 0
    res = []

    for y in range(n):
        grid.append(inp())
        for x in range(n):
            if grid[-1][x] == "1":
                candidates.add((y, x))

    while candidates:
        tmp = candidates.pop()
        cnt = 0
        q.append(tmp)
        while q:
            y, x = q.popleft()
            cnt += 1
            for dy, dx in dt:
                tmpY, tmpX = y + dy, x + dx
                if n > tmpY >= 0 and n > tmpX >= 0 and (tmp:=(tmpY, tmpX)) in candidates:
                    q.append(tmp)
                    candidates.remove(tmp)
        res.append(cnt)
    print(len(res))
    for n in sorted(res):
        print(n)

solution()

# https://www.acmicpc.net/problem/2667