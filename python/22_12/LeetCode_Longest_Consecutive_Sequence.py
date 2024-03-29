class Solution:
    def longestConsecutive(self, nums):
        longestStreak = 0
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            currentStreak = 1
            while i < n - 1:
                if nums[i + 1] == nums[i] + 1:
                    currentStreak += 1
                    i += 1
                elif nums[i + 1] == nums[i]:
                    i += 1
                else:
                    break
            if currentStreak == 1:
                i += 1
            longestStreak = max(longestStreak, currentStreak)
        return longestStreak
      
# https://leetcode.com/problems/longest-consecutive-sequence/
