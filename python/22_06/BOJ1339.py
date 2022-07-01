import sys
from queue import PriorityQueue
res = 0
pq = PriorityQueue()
n = int(sys.stdin.readline())
dataList = [[] for _ in range(8)]       # 각 자릿수를 해당하는 인덱스에 넣을 데이터 리스트
for _ in range(n):
    data = sys.stdin.readline().strip()
    i = 0
    for elem in data[::-1]:             # 입력받은 데이터를 뒤에서부터 한 글자씩 0부터 데이터 리스트에 입력
        dataList[i].append(elem)
        i += 1
idx = 7
while not dataList[idx]:                # 시간을 아끼기 위해 가장 자릿수가 큰 숫자가 있는 인덱스 찾기
    idx -= 1
for i in range(idx, -1, -1):            # 자릿수가 큰 수부터 작은 방향으로 진행
    while dataList[i]:
        data = dataList[i][0]
        dataIdx = 0                     # 가장 큰 비중을 차지하는 숫자를 찾기 위해 숫자를 저장
        for t in range(i, -1, -1):
            while data in dataList[t]:
                dataList[t].remove(data)    # 다른 자릿수에 있는 같은 수를 찾아서 제거
                dataIdx += 10 ** t          # 제거하는 대신 dataIdx에 해당하는 숫자 더함
        pq.put(-dataIdx)                    
cnt = 9
while not pq.empty():
    dataIdx = pq.get()          # 우선순위 큐를 이용해 가장 큰 비중이 있는 숫자부터 출력하고 
    res += cnt * -dataIdx       # cnt를 이용해 9부터 점점 작은 숫자를 곱하게 된다
    cnt -= 1
print(res)

# https://www.acmicpc.net/problem/1339
