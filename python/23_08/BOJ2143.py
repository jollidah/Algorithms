# 두 배열의 합

import sys

def Solution():
    inp = sys.stdin.readline
    target = int(inp())
    n = int(inp())
    aDict = dict()
    aList = [0]
    s = 0
    for num in map(int, inp().split()):
        s += num
        aList.append(s)

    for i in range(n):
        for t in range(i + 1, n + 1):
            if (tmp := aList[t] - aList[i]) in aDict:
                aDict[tmp] += 1 # 갯수
            else:
                aDict[tmp] = 1
    del(aList)

    m = int(inp())
    bList = [0]
    s = 0
    res = 0
    for num in map(int, inp().split()):
        s += num
        for b in bList:
            if (tmp:= target - (s - b)) in aDict:
                res += aDict[tmp]
        bList.append(s)
    return res

if __name__ == "__main__":
    print(Solution())

# https://www.acmicpc.net/problem/2143