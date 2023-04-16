# 최소 스패닝 트리

import sys
from queue import PriorityQueue

input = sys.stdin.readline

v, e = map(int, input().split())
p = list(range(v + 1))
pq = PriorityQueue()

def getParent(a):
    while a != p[a]:
        a = p[a]
    return a
    
def isSameParent(a, b):
    return getParent(a) == getParent(b)
    
def union(a, b):
    pa = getParent(a)
    pb = getParent(b)
    if pa < pb:
        p[pb] = pa
    else:
        p[pa] = pb    

for _ in range(e):
    a, b, c = map(int, input().split())
    pq.put([c, a, b])

res = 0
for _ in range(v - 1):
    while True:
        c, a, b = pq.get()
        if not isSameParent(a, b):
            res += c
            union(a, b)
            break
print(res)

# https://www.acmicpc.net/problem/1197