# 킥다운

import sys

inp = sys.stdin.readline
gear_1 = inp().strip()
gear_2 = [False for _ in range(len(gear_1))] + [i == "2" for i in inp().strip()] + [False for _ in range(len(gear_1))]

n1 = len(gear_1)
n2 = len(gear_2) - 2 * n1

Yee = []
for i in range(n1):
    if gear_1[i] == "2":
        Yee.append(i)

minV = 1e9
for i in range(n1 + n2 + 1):
    fit = True
    for y in Yee:
        if gear_2[y + i]:
            fit = False
            break
    if fit:
        minV = min(minV, max(n1 + n2, n1 + i) - min(i, n1))
print(minV)

# https://www.acmicpc.net/problem/1195