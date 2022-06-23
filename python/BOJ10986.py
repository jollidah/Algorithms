import sys
length, div = map(int, sys.stdin.readline().split())
res = 0
elemList = list(map(int, sys.stdin.readline().split()))
s = sum(elemList)
modList = [0 for i in range(div)]
modList[s % div] += 1                   # 나머지 리스트에 합의 나머지 값을 미리 넣어둔다
for i in range(length):                 # 리스트 합에서 왼쪽부터 한 원소씩 값을 빼고 해당하는 값의 나머지 갯수를 갱신 
    s -= elemList[i]
    modList[s % div] += 1
for i in range(div):
    res += modList[i] * (modList[i] - 1) / 2        # 각 나머지 값을 Combination 연산을 통해 가능한 경우의 수 찾기
print(int(res))

# 나머지 리스트를 만들고 각 인덱스에 Combination 연산을 사용하는 것이 제일 중요한 사고였다

# https://www.acmicpc.net/problem/10986
