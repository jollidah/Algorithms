import sys
length = int(sys.stdin.readline())
res = 0
list = list(map(int, sys.stdin.readline().split()))
s = sum(list)
for i in list:
    s -= i              # 모든 리스트의 합을 구해 합에서 앞에 있는 원소를 빼고 남은 합의 값에 곱하는 방법으로 연산 수를 줄인다
    res += s * i        # 연산수를 줄이는게 중요함
print(res)
