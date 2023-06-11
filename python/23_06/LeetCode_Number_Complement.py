class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        cur = 1
        while num > 1:
            a, b = num//2, num%2
            num = a
            if b == 0:
                ans += cur
            cur *= 2
        return ans
