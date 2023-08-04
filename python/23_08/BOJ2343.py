# 기타 레슨

import sys

def is_enough(comp):
    cnt = 1
    s = 0
    for num in nList:
        s += num
        if s > comp:
            if cnt == m or num > comp:
                return False
            s = num
            cnt += 1
    else:
        return True

inp = sys.stdin.readline
n , m = map(int, inp().split())
nList = list(map(int, inp().split()))
total_sum = sum(nList)
lp = total_sum // m
rp = total_sum
while lp < rp:
    mid = (lp + rp) // 2
    if is_enough(mid):
        rp = mid
    else:
        lp = mid + 1
print(lp)

# https://www.acmicpc.net/problem/2343