# 신기한 키보드

import sys

inp = sys.stdin.readline
lp, rp = 0, 0
pos = [[] for _ in range(26)]
idx = set()
inpString = inp().rstrip()
dp = [len(inpString), len(inpString)]
for t in range(len(inpString)):
    i = ord(inpString[t]) - 97
    idx.add(i)
    if pos[i]:
        if pos[i][0] > t:
            pos[i][0] = t
        elif pos[i][1] < t:
            pos[i][1] = t
    else:
        pos[i] = [t, t]

for t in sorted(idx):
    next_left, next_right = pos[t]
    term = next_right - next_left
    t0 = term + min(dp[0] + abs(lp - next_right), dp[1] + abs(rp - next_right))
    t1 = term + min(dp[0] + abs(lp - next_left), dp[1] + abs(rp - next_left))
    lp, rp = next_left, next_right
    dp = [t0, t1]
print(min(dp))

# https://www.acmicpc.net/problem/1796