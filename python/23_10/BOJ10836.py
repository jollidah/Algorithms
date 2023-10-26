# 여왕벌

import sys

def Solution():
    inp = sys.stdin.readline

    m, n = map(int, inp().split())
    increasingIdx = [0 for _ in range(2 * m)]

    for _ in range(n):
        z, o, _ = map(int, inp().split())
        increasingIdx[z] += 1
        increasingIdx[z + o] += 1

    tmp = 0
    for i in range(2 * m - 1):
        increasingIdx[i] += tmp + 1 
        tmp = increasingIdx[i] - 1
    resX = increasingIdx[m: -1]
    for y in range(m - 1, -1, -1):
        print(increasingIdx[y], *resX)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/10836