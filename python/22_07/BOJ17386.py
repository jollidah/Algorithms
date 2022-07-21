import sys

# ccw 와 외적의 중요성
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
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0\
    and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) < 0:  # 각 선분을 기준으로 각 점을 ccw를 활용해서 반대방향에 있는지 확인한다
    print(1)
else:
    print(0)
# https://www.acmicpc.net/problem/17386
