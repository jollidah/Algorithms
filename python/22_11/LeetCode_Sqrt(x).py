class Solution:
    def mySqrt(self, x: int) -> int:
        tmp = 1
        while tmp * tmp <= x:
            tmp += 1
        return tmp - 1
        
 # https://leetcode.com/problems/sqrtx/submissions/
