import sys
import heapq

n = int(sys.stdin.readline())
hq = []                 # 힙
list = []               # 입력 값을 받은 후 정렬하기 위해 리스트 선언
heapq.heappush(hq, 0)
l = 1
for _ in range(n):
    startTime, endTime = map(int, sys.stdin.readline().split())
    list.append([startTime, endTime])
list.sort()             # 값을 모두 list에 넣은 후 정렬하여 저장
for startTime, endTime in list:
    if hq[0] <= startTime:      # 최소 값이 startTime보다 작다면 같다면 해당 강의실에서 수업을 진행
        heapq.heappushpop(hq, endTime)
    else:                       # 최소값 보다도 startTime이 더 작다면 새로운 강의실을 이용하기 위해 끝나는 시간을 push
        heapq.heappush(hq, endTime)
        l += 1
print(l)    # 힙의 각각의 노드는 강의실을 의미하며 해당 숫자는 끝나는 시간임을 인지하는게 포인트이다

# https://www.acmicpc.net/problem/11000
