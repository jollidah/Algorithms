# 행렬 곱셈 순서

import sys

def Solution():
    def DFS(lp, rp):
        if dp[lp][rp] != 0:
            return dp[lp][rp]
        if lp + 1 == rp:
            dp[lp][rp] = nList[lp][0] * nList[lp][1] * nList[rp][1]
            return dp[lp][rp]

        res = 1e9
        for i in range(lp + 1, rp):
            res = min(res, DFS(lp, i) + DFS(i + 1, rp) + nList[lp][0] * nList[i][1] * nList[rp][1])
        dp[lp][rp] = res
        return dp[lp][rp]

    inp = sys.stdin.readline
    n = int(inp())
    nList = [tuple(map(int, inp().split())) for _ in range(n)] # immutable list는 tuple이 더 빠름

    dp = [[0] * n for _ in range(n)]
    print(DFS(0, n - 1))

if __name__ =="__main__":
    Solution()

# https://www.acmicpc.net/problem/11049
