# 우체국

import sys

def Solution():
    def calc(pos):
        s = 0
        for i in range(n):
            s += abs(d[i] - pos) * p[i]
        return s

    inp = sys.stdin.readline

    n = int(inp())
    d = []
    p = []
    for _ in range(n):
        a, b = map(int, inp().split())
        d.append(a)
        p.append(b)

    lp = min(d)
    rp = max(d)
    while lp < rp:
        mid = (lp + rp) // 2
        if lp == mid:
            break
        if calc(mid) < calc(mid + 1):
            rp = mid
        else:
            lp = mid
    if calc(lp) <= calc(rp):
        print(lp)
    else:
        print(rp)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/2141