# DSLR

import sys
from collections import deque

def DSLR(s, i):
    if i == 1:
        return D(s)
    if i == 2:
        return S(s)
    if i == 3:
        return L(s)
    return R(s)

def D(s):
    return (s * 2) % 10000

def S(s):
    if s == 0:
        return 9999
    return s - 1

def L(s):
    return s % 1000 * 10 + s // 1000

def R(s):
    return (s % 10) * 1000 + s // 10

input = sys.stdin.readline
for ___ in range(int(input().strip())):
    cache = set()
    dq = deque()
    s, t = map(int, input().split())
    # print(s, t)
    dq.append([s, 0])
    cache.add(s)
    while dq:
        s, res = dq.popleft()
        for i in range(1, 5):
            tmpS = DSLR(s, i)
            # print(tmpS, res * 10 + i)
            # input()
            if tmpS not in cache:
                cache.add(tmpS)
                tmpR = res * 10 + i
                if tmpS == t:
                    dq.clear()
                    break
                else:
                    dq.append([tmpS, tmpR])
    for s in str(tmpR):
        if s == "1":
            print("D", end="")
        elif s == "2":
            print("S", end="")
        elif s == "3":
            print("L", end="")
        else:
            print("R", end="")
    print()
    
# https://www.acmicpc.net/problem/9019