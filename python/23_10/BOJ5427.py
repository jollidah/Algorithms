# 불

import sys
from collections import deque

def Solution():
    dt = ((-1, 0), (0, 1), (1, 0), (0, -1))
    inp = sys.stdin.readline

    for _ in range(int(inp())):
        cnt, escape = 1, False
        w, h = map(int, inp().split())
        grid = [inp().strip() for _ in range(h)]
        move = deque()
        fires = deque()
        dp = [[1 for _ in range(w)] for _ in range(h)]
        for y in range(h):
            for x in range(w):
                if grid[y][x] == "@":
                    move.append((y, x))
                    if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                            escape = True
                            print(1)
                    dp[y][x] = 0
                elif grid[y][x] == "*":
                    fires.append((y, x))
                    dp[y][x] = -1

    # 1: can go, 0: visit, -1: fire
        while move and not escape:
            next_fires = deque()
            while fires:
                y, x = fires.popleft()
                for dy, dx in dt:
                    ty, tx = y + dy, x + dx
                    if h > ty >= 0 and w > tx >= 0 and dp[ty][tx] != -1 and grid[ty][tx] != "#":
                        dp[ty][tx] = -1
                        next_fires.append((ty, tx))
            fires = next_fires
            next_move = deque()
            while move and not escape:
                y, x = move.popleft()
                for dy, dx in dt:
                    ty, tx = y + dy, x + dx
                    if dp[ty][tx] == 1 and grid[ty][tx] == ".":
                        if ty == 0 or ty == h - 1 or tx == 0 or tx == w - 1:
                            escape = True
                            print(cnt + 1)
                            break
                        dp[ty][tx] = 0
                        next_move.append((ty, tx))
            move = next_move
            cnt += 1
        if not escape:
            print("IMPOSSIBLE")

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/5427