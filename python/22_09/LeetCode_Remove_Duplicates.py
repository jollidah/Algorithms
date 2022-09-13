class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        l = len(nums)
        cnt = 1
        while i < l - 1:
            if nums[i + 1] == "_":    # "_"을 만난 경우 반복문 종료
                break
            else:
                if nums[i] == nums[i + 1]:    # 숫자가 연속된 경우
                    nums.pop(i)               # 해당 인덱스 숫자를 뽑고
                    nums.append("_")          # "_"를 추가
                else:
                    cnt += 1
                    i += 1
        return cnt
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/
