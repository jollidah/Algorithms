# Longest Square Streak in an Array

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        s = set()
        d = dict()
        for n in nums:
            if n in s:
                d[n ** 2] = d[n] + 1
                s.add(n ** 2)
            else:
                d[n ** 2] = 1
                s.add(n ** 2)
        return -1 if (res:= max(d.values())) == 1 else res

# https://leetcode.com/problems/longest-square-streak-in-an-array/description/
