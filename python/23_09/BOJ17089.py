import sys

inp = sys.stdin.readline

n, m = map(int, inp().split())
friends = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, inp().split())
    friends[a].append(b)
    friends[b].append(a)

