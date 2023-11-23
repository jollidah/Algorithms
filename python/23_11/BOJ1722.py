# 순열의 순서

import sys
import math
from bisect import bisect_left

from collections import deque

def Solution():
    inp = sys.stdin.readline
    n = int(inp())
    rate = math.factorial(n - 1)
    nums = list(range(1, n + 1))

    n_list = deque(list(map(int, inp().split())))
    if n_list.popleft() == 1:
        res = []
        remain = n_list.popleft() - 1
        for i in range(n - 1, -1, -1):
            div, remain = divmod(remain, rate)
            res.append(nums.pop(div))
            try:
                rate //= i
            except:
                pass
        print(*res)
    else:
        res = 0
        for i in range(n - 1, -1, -1):
            num = n_list.popleft()
            idx = bisect_left(nums, num)
            res += rate * idx
            nums.pop(idx)
            try:
                rate //= i
            except:
                pass
        print(res + 1)
if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/1722