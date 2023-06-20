from collections import deque

def solution(maps):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n, m = len(maps), len(maps[0])
    res = []
    visit = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for t in range(m):
            if maps[i][t] != "X" and not visit[i][t]:
                q = deque()
                q.append([i, t])
                visit[i][t] = True
                cnt = int(maps[i][t])
                while q:
                    y, x = q.popleft()
                    for d in range(4):
                        tmpY = y + dy[d]
                        tmpX = x + dx[d]
                        if n > tmpY >= 0 and m > tmpX >= 0 \
                        and maps[tmpY][tmpX] != "X" and not visit[tmpY][tmpX]:
                            visit[tmpY][tmpX] = True
                            cnt += int(maps[tmpY][tmpX])
                            q.append([tmpY, tmpX])
                res.append(cnt)
        print()
    return sorted(res) if res else [-1]
