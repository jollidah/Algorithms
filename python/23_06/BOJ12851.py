# 숨바꼭질 2

import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().split())
if n >= k:
    print(n - k)
    print(1)
    exit(0)
dp = [200000 for _ in range(200000)]

q = deque()
q.append([n, 0])
minC = 0
res = 1

while q:
    p, cnt = q.popleft()
    if p == k:
        minC = cnt
        break
    if 200000 > p >= 0 and dp[p] >= cnt:
        dp[p] = cnt
        tmp = p * 2
        if tmp < k + 2:
            q.append([tmp, cnt + 1])
        q.append([p + 1, cnt + 1])
        q.append([p - 1, cnt + 1])

while q:
    p, cnt = q.popleft()
    if cnt != minC:
        break
    if p == k:
        res += 1
print(minC)
print(res)

# https://www.acmicpc.net/problem/12851