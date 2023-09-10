# 회전 초밥

import sys

def Solution():
    inp = sys.stdin.readline

    n, d, k, c = map(int, inp().split())
    nList = [int(inp()) for _ in range(n)]
    nList = nList + nList[:k - 1]
    recent = {c : 1}

    # initialize
    for i in range(k):
        if nList[i] in recent:
            recent[nList[i]] += 1
        else:
            recent[nList[i]] = 1

    res = len(recent.keys())

    for lp in range(n - 1):
        if recent[nList[lp]] == 1:
            recent.pop(nList[lp])
        else:
            recent[nList[lp]] -= 1
        rp = lp + k
        if nList[rp] in recent:
            recent[nList[rp]] += 1
        else:
            recent[nList[rp]] = 1

        res = max(res, len(recent.keys()))
    print(res)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/2531