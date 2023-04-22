# 순열 사이클

import sys

input = sys.stdin.readline

for _ in range(int(input().strip())):
    n = int(input().strip())
    child = [0] + list(map(int, input().split()))
    # candidates = set(range(1, n + 1))
    cnt = 0
    visit = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not visit[i]:
            while True:
                if visit[child[i]]:
                    cnt += 1
                    break
                else:
                    i = child[i]
                    visit[i] = True
    print(cnt)

# https://www.acmicpc.net/problem/10451