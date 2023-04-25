# 이중 우선순위 큐

import sys
import heapq

for T in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    removed = [False] * k
    maxH, minH = [], []
    for i in range(k):
        op, n = sys.stdin.readline().split()
        n = int(n)

        if op == 'I':
            heapq.heappush(minH, (n, i))
            heapq.heappush(maxH, (-n, i))
            removed[i] = True
        elif n == 1:
            while maxH and not removed[maxH[0][1]]:
                heapq.heappop(maxH)
            if maxH:
                removed[maxH[0][1]] = False
                heapq.heappop(maxH)
        else:
            while minH and not removed[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                removed[minH[0][1]] = False
                heapq.heappop(minH)
    while minH and not removed[minH[0][1]]:
        heapq.heappop(minH)
    while maxH and not removed[maxH[0][1]]:
        heapq.heappop(maxH)
    print(-maxH[0][0], minH[0][0]) if maxH and minH else print("EMPTY")

# https://www.acmicpc.net/problem/7662