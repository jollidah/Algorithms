# 공주님의 정원

import sys

inp = sys.stdin.readline
n = int(inp().rstrip())
accumulate = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
date = 60
target = 334
flowers = []
tmpMax = date
cnt = 0
for _ in range(n):
    sm, sd, em, ed = map(int, inp().split())
    flowers.append([accumulate[sm] + sd, accumulate[em] + ed])
flowers.sort()
# date는 탐색해야 하는 날짜를 포함하고 있음
for start, end in flowers:
    if start > tmpMax:
        print(0)
        break
    if date < start:
            cnt += 1
            date = tmpMax
    tmpMax = max(tmpMax, end)
    if tmpMax > target:
         print(cnt + 1)
         break
else:
    print(0)

# https://www.acmicpc.net/problem/2457