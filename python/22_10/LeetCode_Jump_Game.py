from queue import PriorityQueue

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        isPos = [1] + [0] * (len(nums) - 1) # 초기화를 위해 첫 인덱스를 1
        for i in range(len(nums)):
            if isPos[i] == 1:
                if i + nums[i] >= len(nums) - 1:
                    return True
                for t in range(1, nums[i] + 1):
                    isPos[i + t] = 1
        return False
      
# https://leetcode.com/problems/jump-game/
