import sys

def getParent(a) -> int:
    while a != p[a]:
        a = p[a]
    return a

def union(a, b) -> None:
    pa = getParent(a)
    pb = getParent(b)    
    if pa != pb:
        if pa > pb:
            p[pa] = pb
        else:
            p[pb] = pa

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
p = [i for i in range(n + 1)]

for i in range(1, n + 1):
    target = [0] +list(map(int, sys.stdin.readline().split()))
    for j in range(1, m + 1):
        if target[j] == 1:
            union(i, j)

target = list(map(int, sys.stdin.readline().split()))
res = getParent(target[0])
# print(p)
for i in range(1, m):
    if res != getParent(target[i]):
        print("NO")
        exit(0)
print("YES")