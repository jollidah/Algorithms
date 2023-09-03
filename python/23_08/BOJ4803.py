import sys
from collections import deque

inp = sys.stdin.readline

case_num = 0
while True:
    n, m = map(int, inp().split())
    if n == 0 and m == 0:
        exit(0)
    case_num += 1
    childs = [set() for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        childs[a].add(b)
        childs[b].add(a)
    cnt = 0
    for i in range(1, n + 1):
        if visit[i]:
            continue
        is_tree = True
        q = deque([i])
        visit[i] = True
        while q:
            node = q.popleft()
            for child in childs[node]:
                if visit[child]:
                    is_tree = False
                visit[child] = True
                q.append(child)
                childs[child].discard(node)
        if is_tree:
            cnt += 1
    if cnt == 0:
        print("Case {}: No trees.".format(case_num))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(case_num))
    else:
        print("Case {}: A forest of {} trees.".format(case_num, cnt))
            
            

        
