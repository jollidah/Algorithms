# 가장 긴 증가하는 부분 수열 3

from bisect import bisect_left #이진탐색 코드, 같은 수일 경우 왼쪽 index를 돌려준다
import sys

input = sys.stdin.readline
A = list(map(int, input().split()))
lis = []

for i in A:
    k = bisect_left(lis, i) #자신이 들어갈 위치 k
    if len(lis) == k: #i가 가장 큰 숫자라면
        lis.append(i)
    else:
        lis[k] = i #자신보다 큰 수 중 최솟값과 대체
print(len(lis))

# https://www.acmicpc.net/problem/12738