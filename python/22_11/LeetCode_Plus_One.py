class Solution:
    def plusOne(self, digits):
        idx = len(digits) - 1 # 1의자릿수부터 탐색 시작
        while idx >= 0:
            if digits[idx] == 9:
                digits[idx] = 0
                idx -= 1
            else:
                digits[idx] += 1
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

      
# https://leetcode.com/problems/plus-one/
