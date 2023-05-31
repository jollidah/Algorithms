class Solution:
    def isUgly(self, num: int) -> bool:
        answer = False
        if num <= 0:
            return False
        
        nums = [2, 3, 5]

        for i in nums:
            while num % i == 0:
                num = num / i
        
        if num == 1:
            answer = True
        
        return answer
