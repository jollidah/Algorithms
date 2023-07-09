import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp().rstrip())
accumulate = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
date = accumulate[3] + 1
target = accumulate[11] + 30
flowers = []
tmpMax = 0
cnt = 0
for _ in range(n):
    sm, sd, em, ed = map(int, inp().split())
    flowers.append([accumulate[sm] + sd, accumulate[em] + ed])
flowers.sort()
# print(date, target)
# date는 탐색해야 하는 날짜를 포함하고 있음
for start, end in flowers:
    # print(start, end)
    if tmpMax > target:
        break
    if date < start:
        if tmpMax == 0:
            break
        else:
            cnt += 1
            date = tmpMax
            # print("cnt", date, target)
            if date >= start and date <= end:
                tmpMax = end 
            else:
                tmpMax = 0
    elif date <= end:
        tmpMax = max(tmpMax, end)
        
if date < tmpMax:
    cnt += 1
    date = tmpMax
print(cnt if date > target else 0)
