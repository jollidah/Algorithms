# 레이저 통신

import sys

input = sys.stdin.readline

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solution():
    w, h = map(int, input().split())
    grid = [[*input().rstrip()] for _ in range(h)]
    dp = [[-1]*w for _ in range(h)]
    k = max(w, h)
    target = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'C':
                target.append((r, c))
    q = [target[0]]
    dp[target[0][0]][target[0][1]] = 0
    cnt = 0
    while q:
        next_q = []
        while q:
            r, c = q.pop()
            for dr, dc in delta:
                nr, nc = r+dr, c+dc
                for _ in range(k-1):
                    if h > nr >= 0 and w > nc >= 0 and grid[nr][nc] != '*':
                        if dp[nr][nc] == -1:
                            dp[nr][nc] = cnt
                            next_q.append((nr, nc))
                            if nr == target[1][0] and nc == target[1][1]:
                                print(cnt)
                                return
                        elif dp[nr][nc] < cnt:
                            break
                    else:
                        break
                    nr += dr
                    nc += dc
        q = next_q
        cnt += 1

solution()

# https://www.acmicpc.net/problem/6087