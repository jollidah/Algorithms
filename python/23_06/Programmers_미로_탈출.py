from collections import deque

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n = len(maps)
    m = len(maps[0])
    levers = []
    for y in range(n):
        for x in range(m):
            if maps[y][x] == "L":
                levers.append([y, x])
    res = -1
    for y, x in levers:
        visit = [[False for _ in range(m)] for _ in range(n)]
        d1, d2 = 0, 0
        q = deque()
        q.append([y, x, 0])
        visit[y][x] = True
        while q:
            y, x, cnt = q.popleft()
            if d1 != 0 and d2 != 0:
                break
            for d in range(4):
                tmpY = y + dy[d]
                tmpX = x + dx[d]
                if n > tmpY >= 0 and m > tmpX >= 0 \
                and not visit[tmpY][tmpX] and maps[tmpY][tmpX] != "X":
                    visit[tmpY][tmpX] = True
                    if maps[tmpY][tmpX] == "S":
                        d1 = cnt + 1
                    if maps[tmpY][tmpX] == "E":
                        d2 = cnt + 1
                    q.append([tmpY, tmpX, cnt + 1])
        if d1 != 0 and d2 != 0:
            res = d1 + d2
    return res
        
