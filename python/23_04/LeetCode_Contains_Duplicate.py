class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_table = {}
        for n in nums:
            if n in check_table:
                return True
            else:
                check_table[n] = 1
        return False
