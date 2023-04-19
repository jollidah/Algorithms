# 공유기 설치

import sys

def binarySearch(lp, rp):
    global answer
    while lp < rp:
        cnt = 1
        mid = (lp + rp) // 2
        ex = houses[0]
        for i in range(1, n):
            if houses[i] - ex >= mid:
                ex = houses[i]
                cnt += 1
        if cnt >= c:
            lp = mid + 1
            answer = max(answer, mid)
        else:
            rp = mid

input = sys.stdin.readline

n, c = map(int, input().split())
houses = sorted([int(input().strip()) for _ in range(n)])
cList = list(range(c - 1)) + [n - 1]

answer = 0
binarySearch(1, (houses[-1] - houses[0]) // (c - 1) + 1)
print(answer)

# https://www.acmicpc.net/status?user_id=help0304&problem_id=2110&from_mine=1