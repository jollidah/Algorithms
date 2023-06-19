class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp=[]
        k=k%len(nums)
        temp=nums[-k:]
        nums[k:]=nums[:-k]
        nums[:k]=temp
