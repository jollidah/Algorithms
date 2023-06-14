import sys
from queue import PriorityQueue

inp = sys.stdin.readline
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
n, m = map(int, inp().split())
hList = []
q = PriorityQueue()
for y in range(n):
    hList.append(list(map(int, inp().split())))
    for x in range(m):
        q.put([hList[y][x], y, x])

def getParent(y, x):
    while [y, x] != p[y][x]:
        y, x = p[y][x]
    return y, x

sList = []
dp = [list(map(int, inp().split())) for _ in range(n)]
p = [[[y, x] for x in range(m)] for y in range(n)]

while not q.empty():
    h, y, x = q.get()
    py, px = getParent(y, x)
    tmpParents = [[py, px]]
    for d in range(4):
        tmpY = y + dy[d]
        tmpX = x + dx[d]
        if n > tmpY >= 0 and m > tmpX >= 0:
            if hList[y][x] >= hList[tmpY][tmpX]:
                if (tmpP := list(getParent(tmpY, tmpX))) not in tmpParents:  
                    if hList[py][px] == hList[tmpP[0]][tmpP[1]]:
                         sList.append([py, px, tmpP[0], tmpP[1]])
                    tmpParents.append(tmpP)
                    dp[py][px] += dp[tmpP[0]][tmpP[1]] if dp[tmpP[0]][tmpP[1]] else tList[tmpP[0]][tmpP[1]]
    for i in range(len(tmpParents)):
        p[tmpParents[i][0]][tmpParents[i][1]] = p[py][px]

for i in range(len(sList) - 1, -1, -1):
    dp[sList[i][2]][sList[i][3]] = dp[sList[i][0]][sList[i][1]]

for y in range(n):
    print(*dp[y])
print()

