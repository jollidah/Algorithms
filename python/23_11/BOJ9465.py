# 스티커

import sys

inp = sys.stdin.readline

def Solution(inp):
    for _ in range(int(inp())):
        n = int(inp())
        stickers = [tuple(map(int, inp().split())) for _ in range(2)]
        dp = [[0] * n for _ in range(3)] 
        dp[0][0], dp[1][0], dp[2][0] = stickers[0][0], stickers[1][0], 0
        for i in range(1, n):
            dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + stickers[0][i]
            dp[1][i] = max(dp[0][i - 1], dp[2][i - 1]) + stickers[1][i]
            dp[2][i] = max(dp[0][i - 1], dp[1][i - 1], dp[2][i - 1])
        print(max(map(lambda x: x[n - 1], dp)))
if __name__ == "__main__":
    Solution(inp)

# https://www.acmicpc.net/problem/9465