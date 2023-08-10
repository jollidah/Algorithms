# 보물섬
"G5 / "
import sys
from collections import deque

def Solution():
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    res = 0
    inp = sys.stdin.readline
    n, m = map(int, inp().split())
    land = [[s == "L" for s in inp().rstrip()] for _ in range(n)]
    for y in range(n):
        for x in ra:
            if land[y][x]:
                # 이게 가장 중요했음 
                if 0<=y-1<n and 0<=y+1<n and\
                      land[y-1][x] and land[y+1][x]: continue
                if 0<=x-1<m and 0<=x+1<m and\
                      land[y][x-1] and land[y][x-1]: continue
                q = deque()
                q.append((y, x, 0))
                toVisit = [[True for _ in range(m)] for _ in range(n)]
                toVisit[y][x] = False
                while q:
                    ty, tx, cnt = q.popleft()
                    for d in range(4):
                        tmpY = ty + dy[d]
                        tmpX = tx + dx[d]
                        if n > tmpY >= 0 and m > tmpX >= 0 and \
                        toVisit[tmpY][tmpX] and land[tmpY][tmpX]:
                            toVisit[tmpY][tmpX] = False
                            q.append((tmpY, tmpX, cnt + 1))
                res = max(res, cnt) # 내 주변에 3개 이상의 땅이 있다면난 최소가 아니다
    return(res)

if __name__ == "__main__":  
    print(Solution())

# https://www.acmicpc.net/problem/2589