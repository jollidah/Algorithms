# 두 용약
"골5 / 1h"
import sys
import bisect

def Solution():
    inp = sys.stdin.readline
    n = int(inp())
    pos = []
    neg = []
    zCnt = 0
    for num in list(map(int, inp().split())):
        if num == 0:
            if zCnt == 1:
                return 0, 0
            zCnt += 1
        elif num > 0:
            pos.append(num)
        else:
            neg.append(num)
    pos = sorted(set(pos))
    neg = sorted(set(neg))

    m, r1, r2 = 2e9, 0, 0
    if pos:
        if zCnt != 0:
            m, r1, r2 = pos[0], 0, pos[0]
        elif len(pos) > 1:
            m, r1, r2 = pos[0] + pos[1], pos[0], pos[1]
    if neg:
        if zCnt != 0 and m  > -neg[-1]:
            m, r1, r2 = -neg[-1], neg[-1], 0
        elif len(neg) > 1 and m > -neg[-1] - neg[-2]:
            m, r1, r2 = -neg[-1] - neg[-2], neg[-2], neg[-1]


    if len(pos) < len(neg):
        for num in pos:
            idx = bisect.bisect_left(neg, -num) 
            if idx != len(neg) and m  > abs(num + neg[idx]):
                if idx != 0 and abs(num + neg[idx]) > abs(num + neg[idx - 1]):
                    m, r1, r2 = abs(num + neg[idx - 1]), neg[idx - 1], num
                else:
                    m, r1, r2 = abs(num + neg[idx]), neg[idx], num
            elif idx != 0 and m > abs(num + neg[idx - 1]):
                m, r1, r2 = abs(num + neg[idx - 1]), neg[idx - 1], num
            if m == 0:
                break
    else:
        for num in neg:
            idx = bisect.bisect_left(pos, -num)
            if idx != len(pos) and m  > abs(num + pos[idx]):
                if idx != 0 and abs(num + pos[idx]) > abs(num + pos[idx - 1]):
                    m, r1, r2 = abs(num + pos[idx - 1]), num, pos[idx - 1]
                else:
                    m, r1, r2 = abs(num + pos[idx]), num, pos[idx]
            elif idx != 0 and m > abs(num + pos[idx - 1]):
                m, r1, r2 = abs(num + pos[idx - 1]), num, pos[idx - 1]
            if m == 0:
                break
    return r1, r2

if __name__ == "__main__":
    print(*Solution())

# https://www.acmicpc.net/problem/2470