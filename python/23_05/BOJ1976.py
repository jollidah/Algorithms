# 여행 가자

import sys

def getParent(a):
    while a != p[a]:
        a = p[a]
    return a

def union(a, b):
    pa = getParent(a)
    pb = getParent(b)
    if pa > pb:
        p[pa] = pb
    else:
        p[pb] = pa

inp = sys.stdin.readline
n = int(inp().rstrip())
m = int(inp().rstrip())
p = [i for i in range(n + 1)]
for i in range(n):
    tmp = inp().split()
    for t in range(n):
        if tmp[t] == "1":
            union(i + 1, t + 1)

trip = list(map(int, inp().split()))
target = getParent(trip[0])
for i in range(1, m):
    if target != getParent(trip[i]):
        print("NO")
        exit(0)
print("YES")

# https://www.acmicpc.net/problem/1976