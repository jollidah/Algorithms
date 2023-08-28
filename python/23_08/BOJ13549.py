# 숨바꼭질 3

import sys
from collections import deque

inp = sys.stdin.readline

n, k = map(int, inp().split())

if n >= k:
    print(n - k)
    exit(0)
q = deque([n])
dp = [1e7 for _ in range(k + 1)]
dp[n] = 0
while q:
    num = q.popleft()
    if num == k:
        break
    # case 1
    next = num << 1
    if next >= k:
        dp[k] = min(dp[k], dp[num] + next - k)
    elif dp[next] == 1e7:
        dp[next] = dp[num]
        q.appendleft(next)
    # case 2
    next = num + 1
    if next == k:
        dp[k] = min(dp[num] + 1, dp[k])
    elif dp[next] == 1e7:
        dp[next] = dp[num] + 1
        q.append(next)

    next = num - 1
    if next == k:
        dp[k] = min(dp[num] + 1, dp[k])
    elif next != -1 and dp[next] == 1e7:
        dp[next] = dp[num] + 1
        q.append(next)

print(dp[k])

# https://www.acmicpc.net/problem/13549