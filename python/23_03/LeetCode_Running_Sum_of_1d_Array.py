from itertools import accumulate

class Solution:
    def runningSum(self, nums):
        return list(accumulate(nums))

output = Solution()
print(output.runningSum(list(map(int,input().split(",")))))
