# 미세먼지 안녕!

import sys
from collections import deque

def Solution():
    inp = sys.stdin.readline
    dt = ((-1, 0), (0, 1), (1, 0), (0, -1))

    def combine_buffer():
        while q:
            y, x = q.pop()
            grid[y][x] += buffer[y][x]
            buffer[y][x] = 0

    n, m, t = map(int, inp().split())
    grid = []
    airCleaner = []
    buffer = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    for y in range(n):
        grid.append(list(map(int, inp().split())))
        if grid[-1][0] == -1:
            airCleaner.append(y)
    for _ in range(t):
    # 미세먼지 확산 (4방향, 먼지 // 5)
        for y in range(n):
            for x in range(m):
                if grid[y][x] != -1:
                    floating = grid[y][x] // 5
                    for dy, dx in dt:
                        ty, tx = y + dy, x + dx
                        if n > ty >= 0 and m > tx >= 0 and grid[ty][tx] != -1:
                            q.append((ty, tx))
                            grid[y][x] -= floating
                            buffer[ty][tx] += floating
        combine_buffer()
    # 공기 청정기(그림 참고)
    # Case 1: 위쪽
        for y in range(airCleaner[0] - 1, 0, -1):
            grid[y][0] = grid[y - 1][0]
        tmp_range = range(m - 1) if airCleaner[0] != 0 else range(1, m - 1)
        for x in tmp_range:
            grid[0][x] = grid[0][x + 1]
        for y in range(airCleaner[0]):
            grid[y][m - 1] = grid[y + 1][m - 1]
        for x in range(m - 1, 1, -1):
            grid[airCleaner[0]][x] = grid[airCleaner[0]][x - 1]
        grid[airCleaner[0]][1] = 0
    
    # Case 2: 아래쪽 pass
        for y in range(airCleaner[1] + 1, n - 1):
            grid[y][0] = grid[y + 1][0]
        tmp_range = range(m - 1) if airCleaner[1] != n - 1 else range(1, m - 1)
        for x in tmp_range:
            grid[n - 1][x] = grid[n - 1][x + 1]
        for y in range(n - 1, airCleaner[1], -1):
            grid[y][m - 1] = grid[y - 1][m - 1]
        for x in range(m - 1, 1, -1):
            grid[airCleaner[1]][x] = grid[airCleaner[1]][x - 1]
        grid[airCleaner[1]][1] = 0

    print(sum(map(sum, grid)) + 2)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/17144