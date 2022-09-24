class Solution:
    def firstMissingPositive(self, nums):
        cnt = 1
        nums = set(nums)  # 중복 제거
        nums = list(nums)   # 리스트로 변경
        nums.sort()     # 정렬
        while nums:
            if nums[0] <= 0:  # 음수는 제거
                nums.pop(0)
                continue
            if cnt == nums.pop(0):  # cnt와 같다면 제거 후 cnt + 1
                cnt += 1
            else:
                return cnt
        return cnt
      
  # https://leetcode.com/problems/first-missing-positive/
  
