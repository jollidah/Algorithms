# 다이어트

import sys
import math

def Solution():
    inp = sys.stdin.readline

    target = int(inp())
    rp = int(math.sqrt(target))
    lp = 1
    is_impossible = True

    while (2 *lp + 1) <= target:
        r_num = rp ** 2
        l_num = lp ** 2
        sub = r_num - l_num
        if sub == target:
            is_impossible = False
            print(rp)
            rp += 1
            lp += 1
        elif sub < target:
            rp += 1
        else:
            lp += 1

    if is_impossible:
        print(-1)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/1484