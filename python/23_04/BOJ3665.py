# 최종 순위

import sys
from collections import deque

input = sys.stdin.readline
qr = int(input().strip())
for __ in range(qr):
    n = int(input().strip())
    childs = [set() for _ in range(n + 1)]   # 자식을 저장할 리스트
    indegree = [-1 for _ in range(n + 1)]   # 선행 갯수
    starts = set()              # 시작점을 저장할 집합
    res = []                    # 결과를 저장할 배열
    l = list(map(int, input().split()))
    starts.add(l[0])

    # 자식, 선행 갯수 업데이트
    for i in range(len(l)):
        childs[l[i]] = set(l[i + 1:])
        indegree[l[i]] = i
    # 바뀐 자식, 선행 갯수 업데이트
    for _ in range(int(input().strip())):
        a, b = map(int, input().split())
        if a in childs[b]:
            a, b = b, a
        childs[a].remove(b)
        indegree[a] += 1
        childs[b].add(a)
        indegree[b] -= 1
        if indegree[a] == 0:
            starts.add(a)
        if indegree[b] == 0:
            starts.add(b)

    start = list(filter(lambda x: indegree[x] == 0, starts))
    # 시작 점이 없다면 불가능
    if len(start) == 0:
        print("IMPOSSIBLE")
        continue
    # 시작 점이 여러개라면 순서 지정 불가능
    elif len(start) > 1:
        print("?")
        continue

    dq = deque()
    dq.append(start[0])
    isVisit = [False for _ in range(len(l) + 1)]
    isBreak = False
    isVisit[start[0]] = True
    while dq:
        n = dq.popleft()
        res.append(n)
        isFound = False
        for child in childs[n]:
            # 방문한 적이 있다면 순서가 존재할 수 없음
            if isVisit[child]:
                print("IMPOSSIBLE")
                isBreak = True
                break
            indegree[child] -= 1
            if indegree[child] == 0:
                if not isFound:
                    isFound = True
                    isVisit[child] = True
                    dq.append(child)
                # 같은 순서에 두 개 이상의 child가 발생하면 순서를 지정할 수 없음
                else:
                    print("?")
                    isBreak = True
                    break
            # print(indegree)
    if not isBreak:
        if len(res) == len(l):
            print(*res)
        else:
            # 순서 연결이 끊겼다면 순서를 정할 수 없음
            print("IMPOSSIBLE")

# https://www.acmicpc.net/problem/3665