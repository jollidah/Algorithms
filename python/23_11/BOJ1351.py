# 무한 수열 

import sys

n, p, q = map(int, sys.stdin.readline().split())

d = {}
d[0] = 1
def DFS(n):
    if (n in d):
        return d[n]
    else:
        d[n] = DFS(n//p) + DFS(n//q)
        return d[n]

print(DFS(n))

# https://www.acmicpc.net/problem/1351