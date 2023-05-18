# A Journey to Greece

import sys; input = sys.stdin.readline
import heapq
from math import inf

# 외판원 순회 함수
def dfs(p, v):
    if v == (1 << P) - 1:
        return [matrix[p][0], T]
    if dp[p][v][0] > -1:
        return dp[p][v]
    dp[p][v] = [inf, inf]
    for q in range(P):
        if not v & (1 << q):
            notTaxi, taxi = dfs(q, v | (1 << q))
            dp[p][v][0] = min(dp[p][v][0], matrix[p][q] + notTaxi)
            dp[p][v][1] = min(min(dp[p][v]), matrix[p][q] + taxi, T + notTaxi)
    return dp[p][v]

N, P, M, G, T = map(int, input().split())

# 방문해야 하는 정점들을 입력 받고 좌표 압축 및 P 초기화
site = {0: 0}
stay = zero = 0
for i in range(1, P + 1):
    p, t = map(int, input().split())
    if not p:
        zero += 1
    else: site[p] = i - zero
    stay += t
P = len(site)

# 간선을 입력 받아 graph 만들기 (간선은 양방향)
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# P개의 정점들 간 거리를 담을 행렬을 만들고
# P개의 정점 차례대로 다익스트라를 돌려 행렬에 거리 입력
matrix = [[0] * P for _ in range(P)]
for p, i in site.items(): # 다익스트라할 땐 실제 위치 사용
    distance = [inf] * N
    distance[p] = 0
    queue = []
    heapq.heappush(queue, [0, p])
    while queue:
        d, present = heapq.heappop(queue)
        if distance[present] < d:
            continue
        for nxt, dd in graph[present]:
            if distance[nxt] > distance[present] + dd:
                distance[nxt] = distance[present] + dd
                heapq.heappush(queue, [distance[nxt], nxt])
    for q, j in site.items(): #거리 담을 땐 압축 값 사용
        result = distance[q]
        matrix[i][j] = result
        matrix[j][i] = result

# dp는 3차원으로 만들어야 함
# 현재 위치, 방문한 위치, 택시 고려 유무
dp = [[[-1] * 2 for _ in range(1 << P)] for __ in range(P)]
notTaxi, taxi = dfs(0, 1 << 0)
# 답을 출력할 때, stay 값을 꼭 더해줘야 한다.
print('possible without taxi') if notTaxi + stay <= G else print('possible with taxi') if taxi + stay <= G else print('impossible')

# https://www.acmicpc.net/problem/10849