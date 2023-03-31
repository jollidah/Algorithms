import sys

n, m, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
res = 0
if m < k:                   # m 이 k 보다 작은 경우 그냥 m만큼 제일 큰 수를 곱하게 종료
    res = m * data[-1]
else:
    while m > 0:           
        if m > k:               # k 가 m 보다 작은 경우 k개의 제일 큰 수와 1개의 2번째로 큰 수를 더한다
            res += k * data[-1] + data[-2]  
            m -= k + 1          # 그 이후 m 에서 k + 1개 만큼을 빼준다
        else:
            res += m * data[-1] # k보다 더 적은 숫자가 남았다면 그냥 그 수만큼 제일 큰 수르 더한다
print(res)
