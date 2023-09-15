# 골롱 수열

import sys
from collections import deque

def Solution():
    inp = sys.stdin.readline
    n = int(inp())
    if n < 3:
        print(n)
        exit(0)
    w = deque([1])
    num = 2
    idx = 2
    s = 0
    while n > s:
        cnt  = w.popleft()
        for i in range(cnt):
            w.append(num)
            s += num
        idx += cnt
        num += 1

    while n > idx:
        cnt  = w.popleft()
        idx += cnt
        num += 1
    print(num - 1)

if __name__ == "__main__":
    Solution()
    
# https://www.acmicpc.net/problem/2038