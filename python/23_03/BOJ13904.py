# 과제

import sys
from collections import defaultdict
import heapq
n = int(sys.stdin.readline())
h = []

dd = defaultdict(int)

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    heapq.heappush(h, [-w, -d])
res = 0
while h:
    w, d =  [ -x for x in heapq.heappop(h)]
    while(dd[d] != 0 and d > 0):
        d -= 1
    if d != 0:
        dd[d] = w
        res += w
print(res)

# https://www.acmicpc.net/problem/13904