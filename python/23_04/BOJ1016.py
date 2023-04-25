# 제곱 ㄴㄴ 수

import sys
import math

input = sys.stdin.readline

n , m = map(int, input().split())
start = math.ceil(math.sqrt(n))
end = int(math.sqrt(m)) + 1

start = max(2, start)
s = start
e = int(math.sqrt(end)) + 1
oddList = list(True for _ in range(end + 1))
for i in range(2, e + 1):
    if oddList[i]:
        tmp = i * 2
        while tmp <= end:
            oddList[tmp] = False
            tmp += i
oddNums = []
for i in range(2, end):
    if oddList[i]:
        oddNums.append(i ** 2)
del(oddList)
numList = [True for _ in range(m - n + 1)]
for i in oddNums:
    tmp = (n // i + 1) * i if n % i != 0 else n
    while tmp <= m:
        numList[tmp - n] = False
        tmp += i
cnt = 0
for i in range(m - n + 1):
    if numList[i]:
        cnt += 1
print(cnt)

# https://www.acmicpc.net/problem/1016