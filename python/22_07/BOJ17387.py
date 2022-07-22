import sys


def ccw(xa, ya, xb, yb, xc, yc):
    ans = (xb - xa) * (yc - ya) - (xc - xa) * (yb - ya)
    if ans > 0:
        return 1    # 왼쪽에 있을 때
    elif ans < 0:
        return -1   # 오른쪽에 있을 때
    else:
        return 0    # 같은 선상에 있을 때


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
case1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
case2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
if case1 < 0 and case2 < 0:
    print(1)
    exit()
elif ccw(x1, y1, x2, y2, x3, y3) == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):    # 한 점이 같은 직선 상에 있다면 선분 내에 포함되는지 모든 점 4개를 확인해본다
    print(1)
    exit()
elif ccw(x1, y1, x2, y2, x4, y4) == 0 and min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
    print(1)
    exit()
elif ccw(x3, y3, x4, y4, x1, y1) == 0 and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4):
    print(1)
    exit()
elif ccw(x3, y3, x4, y4, x2, y2) == 0 and min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4):
    print(1)
    exit()
else:
    print(0)
# https://www.acmicpc.net/problem/17387
