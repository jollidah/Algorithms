class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict
        hash_map={}
        for i in range(len(nums)):
            hash_map[nums[i]]=i
        print(hash_map)
        for i in range(len(nums)):
            x=target-nums[i]
            if x in hash_map and hash_map[x]!=i :
                return [i,hash_map[x]]
