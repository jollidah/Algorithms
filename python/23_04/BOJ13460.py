# 구슬 탈출 2

import sys
from collections import deque

def move(ry, rx, by, bx, p):
    if p == 0:
        return up(ry, rx, by, bx)
    if p == 1:
        return right(ry, rx, by, bx)
    if p == 2:
        return down(ry, rx, by, bx)
    if p == 3:
        return left(ry, rx, by, bx)
    
def up(ry, rx, by, bx):
    if hx == bx and hy < by and True not in [isWall[i][hx] for i in range(hy, by + 1)]:
            return [-2, -2, -2, -2]
    if hx == rx and hy < ry and True not in [isWall[i][hx] for i in range(hy, ry + 1)]:
            return [-1, -1, -1, -1]
    if rx == bx:
        if by < ry:
            while not isWall[by - 1][bx]:
                by -= 1
            while not isWall[ry - 1][rx] and ry - 1 != by:
                ry -= 1
        else:
            while not isWall[ry - 1][rx]:
                ry -= 1
            while not isWall[by - 1][bx] and by - 1 != ry:
                by -= 1
    else:
        while not isWall[by - 1][bx]:
                by -= 1
        while not isWall[ry - 1][rx]:
                ry -= 1
    return [ry, rx, by, bx]
    
def down(ry, rx, by, bx):
    if hx == bx and hy > by and True not in [isWall[i][hx] for i in range(by, hy + 1)]:
        return [-2, -2, -2, -2]
    if hx == rx and hy > ry and True not in [isWall[i][hx] for i in range(ry, hy + 1)]:
        return [-1, -1, -1, -1]
    if rx == bx:
        if by > ry:
            while not isWall[by + 1][bx]:
                by += 1
            while not isWall[ry + 1][rx] and ry + 1 != by:
                ry += 1
        else:
            while not isWall[ry + 1][rx]:
                ry += 1
            while not isWall[by + 1][bx] and by + 1 != ry:
                by += 1
    else:
        while not isWall[by + 1][bx]:
                by += 1
        while not isWall[ry + 1][rx]:
                ry += 1
    return [ry, rx, by, bx]
    
def right(ry, rx, by, bx):
    if hy == by and hx > bx and True not in isWall[hy][bx: hx + 1]:
        return [-2, -2, -2, -2]
    if hy == ry and hx > rx and True not in isWall[hy][rx: hx + 1]:
            return [-1, -1, -1, -1]
    if ry == by:
        if bx > rx:
            while not isWall[by][bx + 1]:
                bx += 1
            while not isWall[ry][rx + 1] and rx + 1 != bx:
                rx += 1
        else:
            while not isWall[ry][rx + 1]:
                rx += 1
            while not isWall[by][bx + 1] and bx + 1 != rx:
                bx += 1
    else:
        while not isWall[by][bx + 1]:
            bx += 1
        while not isWall[ry][rx + 1]:
            rx += 1
    return [ry, rx, by, bx]

def left(ry, rx, by, bx):
    if hy == by and hx < bx and True not in isWall[hy][hx: bx + 1]:
            return [-2, -2, -2, -2]
    if hy == ry and hx < rx and True not in isWall[hy][hx: rx + 1]:
            return [-1, -1, -1, -1]
    if ry == by:
        if bx < rx:
            while not isWall[by][bx - 1]:
                bx -= 1
            while not isWall[ry][rx - 1] and rx - 1 != bx:
                rx -= 1
        else:
            while not isWall[ry][rx - 1]:
                rx -= 1
            while not isWall[by][bx - 1] and bx - 1 != rx:
                bx -= 1
    else:
        while not isWall[by][bx - 1]:
            bx -= 1
        while not isWall[ry][rx - 1]:
            rx -= 1
    return [ry, rx, by, bx]

input = sys.stdin.readline
n, m = map(int, input().split())
by, ry, hy, bx, rx, hx = 0, 0, 0, 0, 0, 0
isWall = [[False for _ in range(m)] for __ in range(n)]
isVisit = set()
q = deque()
for y in range(n):
    tmp = input().strip()
    for x in range(m):
        if tmp[x] == "B":
            by , bx = y, x
        elif tmp[x] == "R":
            ry , rx = y, x
        elif tmp[x] == "O":
            hy , hx = y, x
        elif tmp[x] == "#":
            isWall[y][x] = True
q.append([ry, rx, by, bx, 0])
isVisit.add((ry, rx, by, bx))

while q:
    ry, rx, by, bx, cnt = q.popleft()
    for i in range(4):
        tmpry, tmprx, tmpby, tmpbx = move(ry, rx, by, bx, i)
        if tmpry == -1:
            print(cnt + 1)
            exit(0)
        elif tmpry != -2 and cnt < 9:
            if (tmpry, tmprx, tmpby, tmpbx) not in isVisit:
                isVisit.add((tmpry, tmprx, tmpby, tmpbx))
                q.append([tmpry, tmprx, tmpby, tmpbx, cnt + 1])
print(-1)

# https://www.acmicpc.net/problem/13460