
from queue import PriorityQueue


# 1. 시작점에서 모든 최단경로를 찾는다
# 2. A 지점에서 모든 최단경로를 찾는다
# 3. B 지점에서 모든 최단경로를 찾는다.
# 4. 각 지점까지의 최단경로는 각각의 리스트에 저장이 되어 있으므로 같은 인덱스끼리의 합의 최솟값을 구하면 된다.


def solution(n, s, a, b, fares):
    inf = int(1e9)
    spq = PriorityQueue()             # 각 지점에서 이용할 우선순위 큐 선언
    apq = PriorityQueue()
    bpq = PriorityQueue()
    graph = [[] for i in range(n + 1)]      # 경로와 가격을 저장할 2중 리스트
    sList = [inf for i in range(n + 1)]     # 각 리스트에는 해당하는 인덱스 까지의 거리가 저장되어 있다
    sList[s] = 0
    aList = [inf for i in range(n + 1)]
    aList[a] = 0
    bList = [inf for i in range(n + 1)]
    bList[b] = 0
    dist, start, end = 0, 0, 0
    for n1, n2, dist in fares:             # 시작점은 미리 해당하는 큐에 넣어둔다
        if n1 == s:
            spq.put((dist, n2, n1))
        if n2 == s:
            spq.put((dist, n1, n2))
        if n1 == a:
            apq.put((dist, n2, n1))
        if n2 == a:
            apq.put((dist, n1, n2))
        if n1 == b:
            bpq.put((dist, n2, n1))
        if n2 == b:
            bpq.put((dist, n1, n2))
        graph[n1].append([dist, n2])            # 그래프 최신화
        graph[n2].append([dist, n1])
    while not spq.empty():                      # 다익스트라 알고리즘 구현
        dist, end, start = spq.get()
        if sList[start] + dist < sList[end]:
            sList[end] = sList[start] + dist
            for d, e in graph[end]:
                spq.put((d, e, end))
    while not apq.empty():
        dist, end, start = apq.get()
        if aList[start] + dist < aList[end]:
            aList[end] = aList[start] + dist
            for d, e in graph[end]:
                apq.put((d, e, end))
    while not bpq.empty():
        dist, end, start = bpq.get()
        if bList[start] + dist < bList[end]:
            bList[end] = bList[start] + dist
            for d, e in graph[end]:
                bpq.put((d, e, end))
    minValue = inf
    for i in range(1, n + 1):
        if minValue > sList[i] + aList[i] + bList[i]:
            minValue = sList[i] + aList[i] + bList[i]
    return(minValue)

  # https://programmers.co.kr/learn/courses/30/lessons/72413
