# 연산자 끼워넣기

import sys

def Solution():
    inp = sys.stdin.readline
    n = int(inp())
    n_list = list(map(int, inp().split()))
    operators_list = list(map(int, inp().split()))
    operators = (
    (lambda x, y: x + y),
    (lambda x, y: x - y),
    (lambda x, y: x * y),
    (lambda x, y: x // y if x >= 0 else -(-x // y)),
    )
    maxV = -1e10
    minV = 1e10
    def DFS(idx, res):
        nonlocal maxV, minV
        if idx == n:
            maxV = max(maxV, res)
            minV = min(minV, res)
            return
        for i in range(4):
            if operators_list[i]:
                operators_list[i] -= 1
                tmp_res = operators[i](res, n_list[idx])
                DFS(idx + 1, tmp_res)
                operators_list[i] += 1

    DFS(1, n_list[0])
    print(maxV, minV, sep="\n")

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/14888