class Solution:
    def removeElement(self, nums, val):
        for i in range(len(nums)):
            if nums[0] != val:
                nums.append(nums[0])
                del nums[0]
            else:
                del nums[0]
        return len(nums)
