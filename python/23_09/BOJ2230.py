# 수 고르기

import sys
def Solution():
    inp = sys.stdin.readline

    n, m = map(int, inp().split())
    nList = [int(inp()) for _ in range(n)]
    nList.sort()
    lp = 0
    rp = 0
    res = 3e9
    while lp <= rp and rp != n:
        sub_num = nList[rp] - nList[lp]
        if sub_num == m:
            print(m)
            break
        elif sub_num > m:
            res = min(res, sub_num)
            lp += 1
        else:
            rp += 1
    else:
        print(res)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/2230