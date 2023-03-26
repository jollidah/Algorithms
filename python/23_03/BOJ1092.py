# 배

import sys

a = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
toDo = [0 for _ in range(a)]

c.sort()
w.sort()
cPtr = 0
wPtr = 0
while wPtr < b:
    if c[cPtr] >= w[wPtr]:
        toDo[cPtr] += 1
        wPtr += 1
    else:
        if cPtr == a - 1:
            print(-1)
            exit(0)
        else:
            cPtr += 1 

isMove = True
while isMove:
    isMove = False
    for i in range(len(toDo) - 1):
        if toDo[i] > toDo[i + 1]:
            m = toDo[i] + toDo[i + 1]
            toDo[i] = m // 2
            toDo[i + 1] = m - toDo[i]
            isMove = True
print(max(toDo))

# https://www.acmicpc.net/problem/1092