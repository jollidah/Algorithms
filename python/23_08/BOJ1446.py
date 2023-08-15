# 지름길

import sys

def Solution():
    inp = sys.stdin.readline
    n, d = map(int, inp().split())
    dp = [i for i in range(10001)]
    exit = [False for _ in range(10001)]
    shortCut = [[] for _ in range(10001)]

    for _ in range(n):
        s, e, c = map(int, inp().split())
        if c < e - s:
            shortCut[s].append((e, c))
            exit[e] = True

    rec = 0
    for p in range(d + 1):
        if exit[p]:
            dp[p] = min(rec, dp[p])
            rec = dp[p]
        if shortCut[p]:
            for e, c in shortCut[p]:
                dp[e] = min(rec + c, dp[e])
        rec += 1
    return rec - 1

if __name__ == "__main__":
    print(Solution())

# https://www.acmicpc.net/problem/1446