# 인구 이동

import sys
from collections import deque

def solution():
    inp = sys.stdin.readline
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    n, l ,r = map(int, inp().split())
    grid = [list(map(int, inp().split())) for _ in range(n)]
    res = -1
    move = True
    while move:
        res += 1
        move = False
        visit = [[False for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                if not visit[y][x]:
                    visit[y][x] = True
                    s = grid[y][x]
                    cnt = 1
                    idx = 0
                    q = deque([(y, x)])
                    while idx < len(q):
                        ty, tx = q[idx]
                        for dy, dx in d:
                            tmpY, tmpX = ty + dy, tx + dx
                            if n > tmpY >= 0 and n > tmpX >= 0 and not visit[tmpY][tmpX]\
                            and r >= abs(grid[ty][tx] - grid[tmpY][tmpX]) >= l:
                                move = True
                                q.append((tmpY, tmpX))
                                visit[tmpY][tmpX] = True
                                cnt += 1
                                s += grid[tmpY][tmpX]
                        idx += 1
                    s //= cnt
                    for ty, tx in q:
                        grid[ty][tx] = s
    print(res)

solution()

# https://www.acmicpc.net/problem/16234