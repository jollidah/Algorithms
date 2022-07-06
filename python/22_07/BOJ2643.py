import sys

n = int(sys.stdin.readline().strip())
dataList = []
cntList = [0] * n
compoList = [[] for _ in range(n)]
for _ in range(n):
    long, short = map(int, sys.stdin.readline().split())
    if short > long:
        long, short = short, long
    dataList.append([long, short])
dataList.sort(reverse=True)     # 여기서 key=lambda를 쓸 필요가 없었다 오히려 key를 설정하여 같은 인수를 가질 경우 정렬을 제대로 하지 못했다.
for i in range(n - 1):
    for t in range(i + 1, n):
        if dataList[i][1] >= dataList[t][1]:
            compoList[i].append(t)  # 각 인덱스 별로 포함할 수 있는 종이를 저장
for i in range(n-1, -1, -1):
    if not compoList[i]:            # 포함할 수 있는 종이가 없다면 해당 종이의 cnt를 1로 cntList에 저장
        cntList[i] = 1
    else:
        for t in compoList[i]:          # 포함할 수 있는 종이 중에 가장 cnt가 큰 것 + 1로 cntList에 저장
            cntList[i] = max(cntList[i], cntList[t] + 1)    # 이미 정렬을 해뒀기 때문에 예외처리는 할 필요가 없다
print(max(cntList))

# https://www.acmicpc.net/problem/2643
