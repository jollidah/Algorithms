# 도서관

import sys

n , m = map(int, sys.stdin.readline().split())
dList1 = []
dList2 = [0] + list(map(int, sys.stdin.readline().split()))
dList2.sort()
for i in range(len(dList2)):
    if dList2[0] < 0:
        dList1.append(dList2.pop(0))
    else:
        break
dList1.append(0)
maxV = max(max(dList2), -min(dList1))
print(2 * (sum(dList2[-1::-m]) - sum(dList1[0::m])) - maxV)

# https://www.acmicpc.net/problem/1461