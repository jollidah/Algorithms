# 가장 긴 바이토닉 부분 순열

import sys

input = sys.stdin.readline

n = int(input().strip())
nList = list(map(int, input().split()))
reverse_nList = nList[::-1]
ascending = [1 for _ in range(n)]
descending = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if nList[i] > nList[j]:
            ascending[i] = max(ascending[j] + 1, ascending[i])
        if reverse_nList[i] > reverse_nList[j]:
            descending[i] = max(descending[j] + 1, descending[i])

maxV = 0
for i in range(n):
    maxV = max(maxV, ascending[i] + descending[n - 1 - i])
print(maxV - 1)

# https://www.acmicpc.net/status?user_id=help0304&problem_id=11054&from_mine=1