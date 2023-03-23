# 보석 도둑

import sys
import heapq

n , k = map(int, sys.stdin.readline().split())

jewelry = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline().strip()) for _ in range(k)]
tmp = []

jewelry.sort()
bags.sort()

res = 0
for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewelry)[1])
    if tmp:
        res -= heapq.heappop(tmp)
    elif not jewelry:
        break
print(res)

# https://www.acmicpc.net/problem/1202