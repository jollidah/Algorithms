# 네트워크 연결

import sys
import heapq

def Solution():
    inp = sys.stdin.readline

    n = int(inp())
    m = int(inp())
    p = list(range(n + 1))
    heap = []

    def find_parent(a):
        while p[a] != a:
            a = p[a]
        return a

    def union_parent(pa, pb):
        if pa > pb:
            p[pa] = pb
        else:
            p[pb] = pa    

    for _ in range(m):
        a, b, c = map(int, inp().split())
        heapq.heappush(heap, (c, a, b))

    res = 0
    for _ in range(n - 1):
        while True:
            c, a, b = heapq.heappop(heap)
            pa, pb = find_parent(a), find_parent(b)
            if pa != pb:
                union_parent(pa, pb)
                res += c
                break
    print(res)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/1922