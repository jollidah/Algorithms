# Cubeditor

import sys
s = sys.stdin.readline().strip()
maxV = 0
for n in range(len(s) - 1):
    j = 0
    pi = [0 for _ in range(len(s))]
    for i in range(n + 1, len(s)):
        while j > 0 and s[i] != s[j + n]:
            j = pi[j - 1]
        if s[i] == s[j + n]:
            j += 1
            pi[i] = j
    maxV = max(maxV, max(pi))
print(maxV)

# https://www.acmicpc.net/problem/1701