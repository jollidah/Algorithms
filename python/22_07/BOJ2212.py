import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))   # 입력값을 저장할 리스트
res = []      # 간격을 저장할 리스트
data.sort()   # data를 오름차순으로 정렬
for i in range(len(data) - 1):
    res.append(data[i + 1] - data[i])  
res.sort(reverse=True)
print(sum(res[k - 1::]))  # 간격이 큰 것부터 k - 1개를 제거한 리스트의 합

# https://www.acmicpc.net/problem/2212
