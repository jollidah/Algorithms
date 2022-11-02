class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:         # Combination의 수식 표현
            m, n = n, m
        res = 1
        k = n - 1
        n += m - 2
        tmp = n
        while tmp > n - k:
            res *= tmp
            tmp -= 1
        while k > 1:
            res //= k
            k -= 1
        return res
      
# https://leetcode.com/problems/unique-paths/
