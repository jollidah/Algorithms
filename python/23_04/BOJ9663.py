# N-Queen

import sys

def DFS(y, q) -> int:
    if q == n:
        return 1
    res = 0
    l = list(s3)
    for i in l:
        if y + i in s1 and y - i in s2 and i in s3:
            s1.discard(y + i)
            s2.discard(y - i)
            s3.discard(i)
            res += DFS(y + 1, q + 1)
            s1.add(y + i)
            s2.add(y - i)
            s3.add(i)
    return res

n = int(sys.stdin.readline().strip())
s1 = set(range(2 * n - 1))
s2 = set(range(1 - n, n))
s3 = set(range(n))
print(DFS(0, 0))

# https://www.acmicpc.net/problem/9663