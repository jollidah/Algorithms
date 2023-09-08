import sys

inp = sys.stdin.readline
n, m = map(int, inp().split())

def DFS(idx, cnt):
    global res
    if cnt == 3:
        res += 1
    elif idx != n + 1 :
        DFS(idx + 1, cnt)
        if not ban[idx]:
            for b in pair[idx]:
                ban[b] += 1
            DFS(idx + 1, cnt + 1)
            for b in pair[idx]:
                ban[b] -= 1

pair = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, inp().split())
    pair[a].append(b)
    pair[b].append(a)

ban = [0 for _ in range(n + 1)]
res = 0
DFS(1, 0)
print(res)