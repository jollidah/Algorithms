# 로봇 시뮬레이션

import sys

inp = sys.stdin.readline
# S E N W
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
a, b = map(int, inp().split())
n, m = map(int, inp().split())
pos = dict()        # 해당 좌표에 몇번 로봇이 있는지 확인하기 위한 dict 
direction = {"S": 0, "E": 1, "N": 2, "W": 3}    # 입력값에 따라 방향을 int로 변환하기 위한 dict
robots = [[]]   # 입력 로봇 번호와 맞추기 위해 빈 리스트 추가
for num in range(1, n + 1):
    x, y, d = inp().split()
    y, x = int(y), int(x)
    robots.append([int(y), int(x), direction[d]]) 
    pos[(y, x)] = num

for _ in range(m):
    idx, command, time = inp().split()
    idx, time = int(idx), int(time)
    y, x, d = robots[idx]
    if command == "F":  # 전진하는 경우
        del pos[(y, x)] # 현재 위치 삭제
        if d == 0 or d == 2:
            for _ in range(time):
                y += dy[d]
                if (y, x) in pos:   # 연산량을 줄이기 위해서 2가지 경우로 나눔
                    print("Robot %d crashes into robot %d" %((idx), pos[(y, x)]))
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
        pos[(y, x)] = idx   # pos update
        robots[idx] = [y, x, d] # robot 위치 업데이트
    else:
        if command == "L":  # 좌료를 위 아래로 뒤집었기 때문에 회전 방향도 반대
            robots[idx][2] = (d + time) % 4
        else:
            robots[idx][2] = (d - time) % 4
print("OK")

# https://www.acmicpc.net/problem/2174