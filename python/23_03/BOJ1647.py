# 도시 분할 계획

import sys

def getParent(a) -> int:
    while a != p[a]:
        a = p[a]
    return a

def compareParent(a, b) -> bool:
    return getParent(a) == getParent(b)

def union(a, b) -> None:
    pa = getParent(a)
    pb = getParent(b)
    if pa > pb:
        p[pa] = pb
    else:
        p[pb] = pa


n, m = map(int, sys.stdin.readline().split())
p = [i for i in range(n + 1)]
vertex = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    vertex.append([c, a, b])
vertex.sort()

cnt = 0
res = 0
for c, a, b in vertex:
    if not compareParent(a, b):
        cnt += 1
        union(a, b)
        res += c
    if cnt == n - 2:
        break
print(res)

# https://www.acmicpc.net/problem/1647