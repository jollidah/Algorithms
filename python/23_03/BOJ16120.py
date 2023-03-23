# PPAP

import sys

s = sys.stdin.readline().strip()
stack = []
ppap = ["P", "P", "A", "P"]
for i in range(len(s)):
    stack.append(s[i])
    if stack[-4:] == ppap:
        for _ in range(3):
            stack.pop()
if stack == ["P"]:
    print("PPAP")
else:
    print("NP")

# https://www.acmicpc.net/problem/16120