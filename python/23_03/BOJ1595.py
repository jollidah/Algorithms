import sys
from queue import PriorityQueue
from collections import deque

input = sys.stdin.readline

def BFS(start):
    dq = deque()
    dq.append([start ,0])
    visited = [False for _ in range(10001)]
    visited[start] = True
    max_d = 0
    target_node = 0
    while dq:
        cur_n, cur_d = dq.popleft()
        for next_n,next_d  in childs[cur_n]:
            if not visited[next_n]:
                visited[next_n] = True
                if (next_d:= next_d + cur_d) > max_d:
                    max_d = next_d 
                    target_node = next_n
                dq.append([next_n, next_d])
    return [target_node, max_d]
        


childs = [[] for _ in range(10001)]

while True:
    try:
        a, b, c = map(int, input().split())
        childs[a].append([b, c])
        childs[b].append([a, c])
    except:
        break
print(BFS(BFS(1)[0])[1])
