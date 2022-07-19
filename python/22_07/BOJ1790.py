import sys

n, k = map(int, sys.stdin.readline().split())
tmp = 1     # 자릿수를 10진수로 표현
cipher = 1  # 한 숫자당 필요한 자리 -> 100의 자리는 3자리
num = 0  
while k > cipher * tmp * 9:   # 몇의 자리 수인지 확인하지 위한 절차
    k -= cipher * tmp * 9
    tmp *= 10
    cipher += 1
num = tmp + (k - 1) // cipher # 자릿수를 확인했다면 한 숫자당 필요한 자리로 나누어 더하여 해당하는 자릿수에서 몇번째로 큰 수인지 확인 
if num > n:                   # n 보다 크면 -1 출력
    print(-1)
else:
    print(str(num)[(k - 1) % cipher])   # 해당하는 수에서 내가 출력해야하는 숫자의 위치를 파악

# https://www.acmicpc.net/problem/1790
