class Solution:
    def summaryRanges(self, nums):
        
        if not nums:
            return []
        
        start = nums[0] 
        end = nums[0]
        ans = []
        def beautify(a, b):
            if a == b:
                return str(a)
            else:
                return str(a) + "->" + str(b)

        for i in range(1,len(nums)):
            if (nums[i] - nums[i-1]) != 1:
                ans.append(beautify(start,nums[i-1]))
                start = nums[i]
        ans.append(beautify(start, nums[-1]))
        return ans
