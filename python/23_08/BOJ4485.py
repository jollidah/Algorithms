# 녹색 옷 입은 애가 젤다지?

import sys
import heapq

def Solution():
    inp = sys.stdin.readline
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    cnt = 1
    while n:= int(inp()):
        dp = [[300000] * n for _ in range(n)]
        grid = [list(map(int, inp().split())) for _ in range(n)]
        q = [(grid[0][0], 0, 0)]
        res = 0
        while q:
            c, y, x = heapq.heappop(q)
            if y == n - 1 and x == n - 1:
                res = c
                break
            for d in range(4):
                tmpY = y + dy[d]
                tmpX = x + dx[d]
                if n > tmpY >= 0 and n > tmpX >= 0 \
                and dp[tmpY][tmpX] > c + grid[tmpY][tmpX]:
                    dp[tmpY][tmpX] = c + grid[tmpY][tmpX]
                    heapq.heappush(q, (dp[tmpY][tmpX], tmpY, tmpX))
        print("Problem {}: {}".format(cnt, res))
        cnt += 1
if __name__ == "__main__":
    Solution()
# g4 / 30m
# https://www.acmicpc.net/problem/4485
