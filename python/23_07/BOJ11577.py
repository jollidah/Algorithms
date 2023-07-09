# Condition of deep sleep

import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().split())
lights = [i == "1" for i in inp().split()]
q = deque()
cnt = 0
for i in range(n + 1 - k):
    if q and q[0] < i:
        q.popleft()
    if (lights[i] and len(q) % 2 == 0) or (not lights[i] and len(q) % 2 == 1):
        q.append(i + k - 1)
        cnt += 1
for i in range(n + 1 - k, n):
    if q and q[0] < i:
        q.popleft()
    if (lights[i] and len(q) % 2 == 0) or (not lights[i] and len(q) % 2 == 1):
        print("Insomnia")
        break
else:
    print(cnt)

# https://www.acmicpc.net/problem/11577