import sys
from queue import Queue
numCases = int(sys.stdin.readline().strip())
for _ in range(numCases):
    structNum, rootNum = map(int, sys.stdin.readline().split())
    buildTimeList = [0] + list(map(int, sys.stdin.readline().split()))      # 짓는 시간을 저장하는 리스트
    dpTable = [0] * (structNum + 1)                                         # 다익스트라 리스트(최장거리)
    childStructList = [[] for i in range(structNum + 1)]                    # 인덱스별로 자식 노드 저장
    entryList = [0] * (structNum + 1)                                       # 진입차수 저장 -> 위상정렬
    for p in range(rootNum):
        rootStruct, childStruct = map(int, sys.stdin.readline().split())
        childStructList[rootStruct].append(childStruct)
        entryList[childStruct] += 1             # 자신에게 오는 간선만큼 진입차수 +1 
    lastChild = int(sys.stdin.readline())
    q = Queue()
    for i in range(1, structNum + 1):
        if entryList[i] == 0:
            q.put([i, buildTimeList[i]])        # 시작 건물 큐에 삽입
            dpTable[i] = buildTimeList[i]       # dpTable에 시작 건물 초기화
    while not q.empty():
        rootStruct, time = q.get()
        if rootStruct != lastChild:
            for child in childStructList[rootStruct]:                       
                dpTable[child] = max(dpTable[child], time + buildTimeList[child])   # 자신의 자식들의 dpTable을 업로드
                entryList[child] -= 1                                               # 자식들과의 간선을 끊으며 자식들의 진입차수 최신화
                if entryList[child] == 0:                                           # 자식들 중에 진입차수가 0인 경우는 q에 삽입
                    q.put([child, dpTable[child]])
    print(dpTable[lastChild])

# https://www.acmicpc.net/problem/1005
# 위상정렬 개념 -> https://m.blog.naver.com/ndb796/221236874984
