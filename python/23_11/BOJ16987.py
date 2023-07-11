# 계란으로 계란치기

import sys

def Solution():
    inp = sys.stdin.readline

    def DFS(idx, cnt):
        if idx == len(eggs):
            return cnt
        if eggs[idx][0] <= 0:
            return DFS(idx + 1, cnt)
        maxV = cnt

        for i in range(len(eggs)):
            if eggs[i][0] > 0 and i != idx:
                tmpCnt = cnt
                eggs[i][0] -= eggs[idx][1]
                eggs[idx][0] -= eggs[i][1]
                if eggs[i][0] <= 0:
                    tmpCnt += 1
                if eggs[idx][0] <= 0:
                    tmpCnt += 1
                maxV = max(maxV, DFS(idx + 1, tmpCnt))

            # rollback
                eggs[i][0] += eggs[idx][1]
                eggs[idx][0] += eggs[i][1]

        return maxV

    eggs = [list(map(int, inp().split())) for _ in range(int(inp()))]
    print(DFS(0, 0))

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/16987