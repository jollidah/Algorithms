import sys
from queue import Queue

def wind(gearPtr, gear, pos):       # 방향(pos)에 따라 기어포인터를 바꿔주어 회전
    if pos == 1:
        gearPtr[gear] = (gearPtr[gear] - 1) % 8
    else:
        gearPtr[gear] = (gearPtr[gear] + 1) % 8

q = Queue()
gearNum = int(sys.stdin.readline().strip())
gearList = [[]]
gearPtr = [0] * (gearNum + 1)
for i in range(gearNum):
    gearList.append(sys.stdin.readline().strip())
numCases = int(sys.stdin.readline().strip())
for _ in range(numCases):
    gear, pos = map(int, sys.stdin.readline().split())
    q.put([gear, pos])
    isVisited = [True] + [False] * (gearNum)    # 방문했던 기어인지 리스트를 통해 기억 & 입력마다 초기화
    while not q.empty():
        gear, pos = q.get()
        if gear < gearNum:        
            if isVisited[gear + 1] == False:    # 아직 방문하지 않았다면
                if gearList[gear][(gearPtr[gear] + 2) % 8] != gearList[gear + 1][(gearPtr[gear + 1] - 2) % 8]:  # 기어포인터를 이용해 극이 다른지 확인
                    q.put([gear + 1, -pos])         # 큐에 다음 기어와 회전 방향을 넣는다
        if 1 < gear:
            if isVisited[gear - 1] == False:
                if gearList[gear][(gearPtr[gear] - 2) % 8] != gearList[gear - 1][(gearPtr[gear - 1] + 2) % 8]:
                    q.put([gear - 1, -pos])
        wind(gearPtr, gear, pos)        # 좌우를 확인했다면 기어를 회전시킨다
        isVisited[gear] = True          # 방문했던 기어 저장
cnt = 0
for p in range(1, gearNum + 1):
    if gearList[p][gearPtr[p]] == "1":
        cnt += 1
print(cnt)
