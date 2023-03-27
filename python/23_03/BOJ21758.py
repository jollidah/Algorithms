# 꿀 따기

import sys 

def calc(b1, b2, h):
    return l[b1:] + l[b2:] - l[b1] - 2 * l[b2]

n = int(sys.stdin.readline().strip())
l = list(map(int, sys.stdin.readline().split()))
if len(l) == 3:
    print(2 * max(l))
    exit(0)

if len(l) == 3:
    print(2 * max(l))

b1 = 0
b2 = 2
h = len(l) - 1
s = 2 * sum(l[2:])
maxV = s
while b2 < h:
    s = s - 2 * l[b2] + l[b2 - 1]
    maxV = max(s, maxV)
    b2 += 1

b1 = len(l) - 1
b2 = len(l) - 3
h = 0
s = 2 * sum(l[:-2])
maxV = max(s, maxV)
while b2 > h:
    s = s - 2 * l[b2] + l[b2 + 1]
    maxV = max(s, maxV)
    b2 -= 1
print(maxV)

# https://www.acmicpc.net/problem/21758