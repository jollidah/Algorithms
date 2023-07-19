# 후보 추천하기

import sys
import heapq
from collections import defaultdict

inp = sys.stdin.readline
n = int(inp())
m = int(inp())
recommend = inp().split()
candidates = dict()
q = []
del_cnt = defaultdict(int)
cnt = 0

for i in range(m):
    num = recommend[i]
    if num not in candidates:
        if cnt == n:
            while del_cnt[(tmp:=heapq.heappop(q)[2])]:
                del_cnt[tmp] -= 1
            del candidates[tmp]
            cnt -= 1
        heapq.heappush(q, (1, i, num))
        candidates[num] = [1, i]
        cnt += 1
    else:
        candidates[num][0] += 1
        del_cnt[num] += 1
        heapq.heappush(q, (candidates[num][0], candidates[num][1], num))
print(*sorted(map(int, candidates.keys())))

# https://www.acmicpc.net/problem/1713