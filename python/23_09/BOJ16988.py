# Baaaaaaaaaduk2

import sys
from collections import deque

def Solution():
    inp = sys.stdin.readline

    n, m = map(int, inp().split())
    candidates = []
    grid = [inp().split() for _ in range(n)]

    def check(y1, x1, y2, x2):
        res = 0
        visit = [[False for _ in range(m)] for _ in range(n)]
        for y, x in [(y1 + dy, x1 + dx) for dy, dx in dt] + [(y2 + dy, x2 + dx) for dy, dx in dt]:
            if n > y >= 0 and m > x >= 0 and not visit[y][x] and grid[y][x] == "2":
                visit[y][x] = True
                q = deque([(y, x)])
                flag = True
                cnt = 1
                while q:
                    ty, tx = q.popleft()
                    for dy, dx in dt:
                        tmpY, tmpX = ty + dy, tx + dx
                        if n > tmpY >= 0 and m > tmpX >= 0 and not visit[tmpY][tmpX]:
                            if grid[tmpY][tmpX] == "0":
                                flag = False
                            elif grid[tmpY][tmpX] == "2":
                                cnt += 1
                                q.append([tmpY, tmpX])
                                visit[tmpY][tmpX] = True
                if flag:
                    res += cnt
        return res

    maxV = 0
    dt = ((-1, 0), (1, 0), (0, 1), (0, -1))
    for y in range(n):
        for x in range(m):
            if grid[y][x] == "0":
                for dy, dx in dt:
                    tmpY, tmpX = y + dy, x + dx
                    if n > tmpY >= 0 and m > tmpX >= 0 and grid[tmpY][tmpX] != "0":
                        candidates.append([y, x])
                        continue

    for i in range(len(candidates) - 1):
        for t in range(i + 1, len(candidates)):
            y1, x1 = candidates[i]
            y2, x2 = candidates[t]
            grid[y1][x1] = "1"
            grid[y2][x2] = "1"
            maxV = max(maxV , check(y1, x1, y2, x2))
            grid[y1][x1] = "0"
            grid[y2][x2] = "0"

    return maxV
if __name__ == "__main__":
    print(Solution())

# https://www.acmicpc.net/problem/16988