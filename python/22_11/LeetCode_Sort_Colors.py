from queue import Queue

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        q = Queue()
        q.put([0, len(nums) - 1])
        while not q.empty():
            i, j = q.get()
            if i >= j:
                continue
            p = nums[i]
            l, r = i, j
            while l < r:
                while l < j and p >= nums[l]:
                    l += 1
                while i < r and p < nums[r]:
                    r -= 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[i], nums[r] = nums[r], nums[i]
            q.put([i, r - 1])
            q.put([r + 1, j])

            
# https://leetcode.com/problems/sort-colors/
