# 전화번호 목록

import sys

def solution():
    inp = sys.stdin.readline
    def contain_num(idx):
        for i in range(10):
            if nList[idx][i] == "#":
                return True
            elif nList[idx][i] != nList[idx + 1][i]:
                return False
        return False

    t = int(inp())
    for _ in range(t):
        n = int(inp())
        nList = []
        for __ in range(n):
            nList.append(inp().rstrip().ljust(10, "#"))
        nList.sort()
        for i in range(n - 1):
            if contain_num(i):
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    solution()

# https://www.acmicpc.net/problem/5052