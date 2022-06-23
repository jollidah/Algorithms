import sys
from queue import PriorityQueue

ballNum = int(sys.stdin.readline())
que = PriorityQueue(maxsize=ballNum)
color_size_list = [0 for i in range(ballNum + 1)]
res = [0 for t in range(ballNum)]
s, exSize, exColor, exIdx, sameCount = 0, 0, -1, 0, 0       # 힙에서 get을 할 때마다 전 변수와 비교하기 위해 전 변수를 저장할 값 선언
for idx in range(ballNum):
    color, size = map(int, sys.stdin.readline().split())
    que.put((size, color, idx))
for _ in range(ballNum):
    size, color, idx = que.get()
    res[idx] = s - color_size_list[color]         # 결과값 =  총합 - 색의 합 (크기는 비교하지 힙을 사용하기 때문에 비교할 필요가 없다)
    if size == exSize:                            # 예외처리 -> 같은 값이 있을 경우 예외 처리가 필요하다 색이 같을 경우와 다를 경우를 다르게 처리해야 한다.
        sameCount += 1
        if color != exColor:                      # 색이 다를 경우: sameCount를 이용해 다른 색 중에 같은 크기를 가진 공의 크기만큼 빼준다
            res[idx] -= exSize * sameCount
        else:                                     # 색이 같을 경우: 전 변수의 값을 그냥 입력시켜 버린다
            res[idx] = res[exIdx]
    else:
        sameCount = 0
    s += size
    exSize, exColor, exIdx = size, color, idx     # 변수들 최산화
    color_size_list[color] += size
for elem in res:
    print(elem)

# https://www.acmicpc.net/problem/10800
