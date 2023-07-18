# 로봇 시뮬레이션

import sys

inp = sys.stdin.readline
# S E N W
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
a, b = map(int, inp().split())
n, m = map(int, inp().split())
pos = dict()

robots = [[]]
for num in range(1, n + 1):
    dir = 0
    x, y, d = inp().split()
    y, x = int(y), int(x)
    if d == "E":
        dir = 1
    elif d == "N":
        dir = 2
    elif d == "W":
        dir = 3
    robots.append([int(y), int(x), dir])
    pos[(y, x)] = num

for _ in range(m):
    idx, command, time = inp().split()
    idx, time = int(idx), int(time)
    y, x, d = robots[idx]
    if command == "F":
        del pos[(y, x)]
        if d == 0 or d == 2:
            for _ in range(time):
                y += dy[d]
                if (y, x) in pos:
                    print("Robot %d crashes into robot %d" %(idx, pos[(y, x)]))
                    exit(0)
                if b + 1 == y or y == 0:
                    print("Robot %d crashes into the wall" %idx)
                    exit(0)
        else:
            for _ in range(time):
                x += dx[d]
                if (y, x) in pos:
                    print("Robot %d crashes into robot %d" %(idx, pos[(y, x)]))
                    exit(0)
                if a + 1 == x or x == 0:
                    print("Robot %d crashes into the wall" %idx)
                    exit(0)
        pos[(y, x)] = idx
        robots[idx] = [y, x, d]
    else:
        if command == "L":
            robots[idx][2] = (d + time) % 4
        else:
            robots[idx][2] = (d - time) % 4
print("OK")

# https://www.acmicpc.net/problem/2174