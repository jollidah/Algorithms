import sys

numTestCases = int(sys.stdin.readline())
dpList = [list(map(int, sys.stdin.readline().split()))] # 각 집으로 가는 동안 해당하는 RGB에서 최솟값을 저장하기 위한 DPList

for i in range(1, numTestCases):
    data = list(map(int, sys.stdin.readline().split()))
    data[0] += min(dpList[i - 1][1], dpList[i - 1][2])
    data[1] += min(dpList[i - 1][0], dpList[i - 1][2])
    data[2] += min(dpList[i - 1][0], dpList[i - 1][1])
    dpList.append(data)

print(min(dpList[numTestCases - 1]))


# https://www.acmicpc.net/problem/1149
