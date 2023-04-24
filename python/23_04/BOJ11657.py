# 타임머신

import sys

def bf(start):
    dist[start] = 0
    # n - 1만큼 반복해야 함
    for i in range(n):
        # 모든 간선들을 확인하기 위함
        for cur, next, cost in vertexes:
            if dist[cur] != 1e9 and dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False
    
input = sys.stdin.readline

n, m = map(int, input().split())
vertexes = []
dist = [1e9 for _ in range(n + 1)]

for _ in range(m):
    vertexes.append(list(map(int, input().split())))

if bf(1):
    print(-1)
else:
    for i in range(2, n + 1):
        print(dist[i] if dist[i] != 1e9 else -1)

# https://www.acmicpc.net/problem/11657