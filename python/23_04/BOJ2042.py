# 구간 합 구하기

import sys

def init(start, end, nodeNum):
    if start == end:
        tree[nodeNum] = inputList[start]
        return tree[nodeNum]
    mid = (start + end) // 2
    tree[nodeNum] = init(start, mid, nodeNum * 2) + init(mid + 1, end, nodeNum * 2 + 1)
    return tree[nodeNum]

def tree_sum(start, end, nodeNum, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[nodeNum]
    mid = (start + end) // 2
    return tree_sum(start, mid, nodeNum * 2, left, right) + tree_sum(mid + 1, end, nodeNum * 2 + 1, left, right)

def update(start, end, nodeNum, idx, fixed):
    if idx < start or idx > end:
        return
    tree[nodeNum] += fixed
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, nodeNum * 2, idx, fixed)
    update(mid + 1, end, nodeNum * 2 + 1, idx, fixed)

input = sys.stdin.readline
n, m, k = map(int, input().split())
tree = [0 for _ in range(4 * n)]
inputList = [0]

for _ in range(n):
    inputList.append(int(input().strip()))
init(1, n, 1)
for _ in range(k + m):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - inputList[b]
        inputList[b] = c
        update(1, n, 1, b, tmp) 
    else:
        print(tree_sum(1, n, 1, b, c))

# https://www.acmicpc.net/problem/2042