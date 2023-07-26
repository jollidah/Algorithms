# 게리맨더링

import sys
from collections import deque
import heapq

inp = sys.stdin.readline

def is_possible(path):
    start = 1
    for i in range(1, n + 1):
        start <<= 1
        if path & start:
            path -= start
            q.append(i)
            break
    while q:
        node = q.popleft()
        for c in connections[node]:
            if path & (tmp := 1 << c):
                path -= tmp
                q.append(c)
    if path:
        return False
    return True


n = int(inp())
population = [0] + list(map(int, inp().split()))
connections = [[]]
totalPopulation = sum(population)
for y in range(n):
    connections.append(list(map(int, inp().split()))[1:])
heap= []

q = deque()
q.append([1, 0, 0])
while q:
    idx, cost, visit = q.popleft()
    if idx == n + 1:
        heapq.heappush(heap, [abs(totalPopulation - 2 * cost), visit])
        continue
    q.append([idx + 1, cost, visit])
    q.append([idx + 1, cost + population[idx], visit + (1 << idx)])

while heap:
    cost, visit = heapq.heappop(heap)
    exclusive = (((1 << (n + 1)) - 1) ^ visit) - 1
    if is_possible(visit) and is_possible(exclusive):
        print(cost)
        break
else:
    print(-1)

# https://www.acmicpc.net/problem/17471