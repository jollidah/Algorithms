# 축사 배정

import sys

def DFS(cowNum):
    if cowNum == -1 or put[cowNum]:
        return 0
    put[cowNum] = True
    for want in cow[cowNum]:
        if barn[want] == -1 or DFS(barn[want]):
            barn[want] = cowNum
            return 1
    return 0
        

inp = sys.stdin.readline
n, m = map(int, inp().split())
cow = [[] + list(map(int, inp().split()[1:])) for _ in range(n)]
barn = [-1 for _ in range(m + 1)]

for i in range(n):
    put = [False for _ in range(n)]
    DFS(i)

print(m + 1 - barn.count(-1))

# https://www.acmicpc.net/problem/2188