# 팰린드롬?

import sys

input = sys.stdin.readline

n = int(input().strip())
nList = list(map(int, input().split()))
dp = [[i for _ in range(2)] for i in range(n + 1)]

p = 0
while p < n:
    # case 1 -> 간격이 홀수
    lp = p - 1
    rp = p + 1
    while lp >= 0 and rp < n and nList[lp] == nList[rp]:
        lp -= 1
        rp += 1
    dp[p + 1][0] = rp

    # case 2 -> 간격이 짝수
    lp = p
    rp = p + 1
    while lp >= 0 and rp < n and nList[lp] == nList[rp]:
        lp -= 1
        rp += 1
    dp[p + 1][1] = rp
    p += 1

for _ in range(int(input().strip())):
    s, e = map(int, input().split())
    mid = (s + e) // 2
    idx = 0
    if (s + e) % 2 != 0:
        idx = 1
    if dp[mid][idx] >= e:
        print(1)
    else:
        print(0)

# https://www.acmicpc.net/problem/10942