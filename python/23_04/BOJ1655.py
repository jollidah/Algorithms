# 가운데를 말해요

import sys
from queue import PriorityQueue

input = sys.stdin.readline
testCases = int(input().strip())
sq = PriorityQueue()
bq = PriorityQueue()
n = int(input().strip())
print(n)
isOdd = True

for _ in range(testCases - 1):
    tmp = int(input().strip())
    # 홀수
    if isOdd:
        isOdd = False
        if n <= tmp:
            bq.put(tmp)
        else:
            bq.put(n)
            sq.put(-1 * tmp)
            n = -1 * sq.get()
    # 짝수
    else:
        isOdd = True
        if n < tmp:
            bq.put(tmp)
            sq.put(-1 * n)
            n = bq.get()
        else:
            sq.put(-1 * tmp)
    print(n)

# https://www.acmicpc.net/problem/1655