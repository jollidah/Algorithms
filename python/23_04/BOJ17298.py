# 오큰수

import sys
import heapq

input = sys.stdin.readline
n = int(input().strip())
nList = list(map(int, input().split()))
heap = []
res = [-1 for _ in range(n)]
heapq.heappush(heap, (nList[0], 0))

for i in range(1, n):
    if nList[i - 1] < nList[i]:
        while heap:
            num, idx = heap[0]
            if num < nList[i]:
                res[idx] = nList[i]
                heapq.heappop(heap)
            else:
                break
    heapq.heappush(heap, (nList[i], i))

print(*res)

# https://www.acmicpc.net/problem/17298