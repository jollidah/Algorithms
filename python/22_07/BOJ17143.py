from sys import stdin
import heapq


def sharkMove(posList):
    gameTable = [[0 for _ in range(C + 1)] for _ in range(R + 1)]   # 상어들의 바뀐 위치를 저장할 지역변수 -> 겹치는지 확인하기 위해
    for i in range(M):
        y, x, speed, pos, size = posList[i]
        if y * x == 0:
            continue
        if pos == 1:
            tmpSpeed = speed % (2 * (R - 1))    # 수식은 생략
            if y - tmpSpeed >= 1:
                y -= tmpSpeed
            else:
                if 2 + tmpSpeed - y > R:
                    y = 2 * R - 2 - tmpSpeed + y
                else:
                    y = 2 + tmpSpeed - y
                    pos = 2
        elif pos == 2:
            tmpSpeed = speed % (2 * (R - 1))
            if y + tmpSpeed <= R:
                y += tmpSpeed
            else:
                if 2 * R - tmpSpeed - y < 1:
                    y = 2 + tmpSpeed + y - 2 * R
                else:
                    y = 2 * R - tmpSpeed - y
                    pos = 1
        elif pos == 3:
            tmpSpeed = speed % (2 * (C - 1))
            if x + tmpSpeed <= C:
                x += tmpSpeed
            else:
                if 2 * C - tmpSpeed - x < 1:
                    x = 2 + tmpSpeed + x - 2 * C
                else:
                    x = 2 * C - tmpSpeed - x
                    pos = 4
        else:
            tmpSpeed = speed % (2 * (C - 1))
            if x - tmpSpeed >= 1:
                x -= tmpSpeed
            else:
                if 2 + tmpSpeed - x > C:
                    x = 2 * C - 2 - tmpSpeed + x
                else:
                    x = 2 + tmpSpeed - x
                    pos = 3
        if gameTable[y][x] != 0:            # 상어가 겹칠 경우 개체의 크기를 비교
            cmpSize, cmpIdx = gameTable[y][x]
            if cmpSize > size:
                posList[i] = [0, 0, 0, 0, 0]
            else:
                posList[cmpIdx] = [0, 0, 0, 0, 0]       
                posList[i] = [y, x, speed, pos, size]
                gameTable[y][x] = [size, i]
        else:
            posList[i] = [y, x, speed, pos, size]
            gameTable[y][x] = [size, i]



input = stdin
R, C, M = map(int, input.readline().split())
posList = []            # 상어의 좌표, 속도, 방향, 크기 등을 저장할 리스트
for idx in range(M):
    y, x, speed, pos, size = map(int, input.readline().split())
    posList.append([y, x, speed, pos, size])
sum = 0
for p in range(1, C + 1):
    sameXList = []
    for i in range(M):
        y, x, speed, pos, size = posList[i]     # 같은 열에 있는 상어들을 찾고 가장 가까운 상어를 찾는 과정
        if x == p:
            heapq.heappush(sameXList, [y, size, i])     # 리스트의 첫 요소 실수 조심
    if sameXList:
        y, size, idx = sameXList[0]
        posList[idx] = [0, 0, 0, 0, 0]
        sum += size
    sharkMove(posList)
print(sum)
# https://www.acmicpc.net/problem/17143
