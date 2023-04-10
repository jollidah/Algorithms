# 고기잡이

import sys
from functools import lru_cache

input = sys.stdin.readline

n, l, m = map(int, input().split())
nets = [[x, l // 2 - x] for x in range(1, l // 2)]
    
fishes = []

@lru_cache
def calc(tmpY, ty, tmpX, tx):
    cnt = 0
    for fy, fx in fishes:
        if tmpY >= fy >= ty and tmpX >= fx >= tx:
            cnt += 1
    return cnt


for _ in range(m):
    fishes.append(list(map(int, input().split())))

maxV = 0
for fy, fx in fishes:
    for ny, nx in nets:
        ty = fy
        tmpY = fy + ny
        tx = fx
        tmpX = fx + nx

        # 그물 왼쪽으로 이동
        for i in range(nx + 1):
            if n >= tmpY and ty >= 1 and n >= tmpX and tx >= 1:
                maxV = max(maxV, calc(tmpY, ty, tmpX, tx))
            if tx == 1:
                break
            tx -= 1
            tmpX -= 1
        
        # 그물 위로 이동
        for i in range(ny + 1):
            if n >= tmpY and ty >= 1 and n >= tmpX and tx >= 1:
                maxV = max(maxV, calc(tmpY, ty, tmpX, tx))
            if ty == 1:
                break
            ty -= 1
            tmpY -= 1

        # 그물 오른쪽으로 이동
        for i in range(nx + 1):
            if n >= tmpY and ty >= 1 and n >= tmpX and tx >= 1:
                maxV = max(maxV, calc(tmpY, ty, tmpX, tx))
            if tmpX == n:
                break
            tx += 1
            tmpX += 1
        
        # 그물 아래로 이동
        for i in range(ny + 1):
            if n >= tmpY and ty >= 1 and n >= tmpX and tx >= 1:
                maxV = max(maxV, calc(tmpY, ty, tmpX, tx))
            if tmpY == n:
                break
            ty += 1
            tmpY += 1
print(maxV) 

# https://www.acmicpc.net/problem/7573