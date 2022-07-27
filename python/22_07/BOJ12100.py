from collections import deque
from copy import deepcopy
import sys


def moveLeft(Table):
    for y in range(n):
        tmp = deque()
        res = []
        for x in range(n):
            if Table[y][x] != 0:        # 0은 무시한다
                tmp.append(Table[y][x])
        while len(tmp) > 1:
            if tmp[0] == tmp[1]:        # 같은 경우 두 요소를 pop하고 2를 곱한 값을 res에 넣어둔다
                res.append(tmp.popleft() << 1)
                tmp.popleft()
            else:
                res.append(tmp.popleft())   # 다른 경우 한 요소만 pop 하여 res에 그대로 넣어둔다
        if tmp:
            res.append(tmp.popleft())   # 혹시 tmp에 요소가 남아있다면 pop하여 res에 그대로 넣어둔다
        Table[y] = res + ([0] * (n - len(res)))
    return Table

def moveRight(Table):
    for y in range(n):
        tmp = deque()
        res = []
        for x in range(n):
            if Table[y][x] != 0:
                tmp.append(Table[y][x])
        while len(tmp) > 1:
            if tmp[-1] == tmp[-2]:
                res.insert(0, tmp.pop() << 1)
                tmp.pop()
            else:
                res.insert(0, tmp.pop())
        if tmp:
            res.insert(0, tmp.pop())
        Table[y] = ([0] * (n - len(res))) + res
    return Table

def moveUp(Table):
    for x in range(n):
        tmp = deque()
        res = deque()
        for y in range(n):
            if Table[y][x] != 0:
                tmp.append(Table[y][x])
        while len(tmp) > 1:
            if tmp[0] == tmp[1]:
                res.append(tmp.popleft() << 1)
                tmp.popleft()
            else:
                res.append(tmp.popleft())
        if tmp:
            res.append(tmp.popleft())
        for i in range(n):
            if res:
                Table[i][x] = res.popleft()
            else:
                Table[i][x] = 0
    return Table


def moveDown(Table):
    for x in range(n):
        tmp = deque()
        res = deque()
        for y in range(n):
            if Table[y][x] != 0:
                tmp.append(Table[y][x])
        while len(tmp) > 1:
            if tmp[-1] == tmp[-2]:
                res.insert(0, tmp.pop() << 1)
                tmp.pop()
            else:
                res.insert(0, tmp.pop())
        if tmp:
            res.insert(0, tmp.pop())
        for i in range(n - 1, -1, -1):
            if res:
                Table[i][x] = res.pop()
            else:
                Table[i][x] = 0
    return Table


def dfs(Table, cnt):
    global ans
    if cnt == 5:
        ans.append(max(map(max, Table)))        # 이차원 배열에서는 max가 다르게 작용한다는 것을 생각하지 못해 시간을 버렸다
        return
    dfs(moveLeft(deepcopy(Table)), cnt + 1)
    dfs(moveRight(deepcopy(Table)), cnt + 1)
    dfs(moveDown(deepcopy(Table)), cnt + 1)
    dfs(moveUp(deepcopy(Table)), cnt + 1)


n = int(sys.stdin.readline().strip())
gameTable = []
ans = []
for _ in range(n):
    gameTable.append(list(map(int, sys.stdin.readline().split())))
dfs(gameTable, 0)
print(max(ans))

# https://www.acmicpc.net/problem/12100
