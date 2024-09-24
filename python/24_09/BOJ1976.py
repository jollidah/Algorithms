import sys

def solution():
    def get_parent(a):
        while a != p[a]:
            a = p[a]
        return a

    def union_parent(a, b):
        pa, pb = get_parent(a), get_parent(b)
        p[pa], p[pb] = (pa, pa) if pa > pb else (pb, pb)

    inp = sys.stdin.readline
    n = int(inp())
    m, p = int(inp()), list(range(n))
    for i in range(n):
        n_list = list(map(int, inp().split()))
        for j in range(i + 1, n):
            if n_list[j] == 1:
                union_parent(i, j)
    to_visit = list(map(int, inp().split()))
    parent = get_parent(to_visit[0] - 1)
    for i in range(1, m):
        if parent != get_parent(to_visit[i] - 1):
            print("NO")
            exit(0)
    print("YES")
    
if __name__ == "__main__":
    solution()
