class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sumList = [nums[0]]
        for i in range(1, len(nums)):
            sumList.append(sumList[i - 1] + nums[i])      # 합 리스트 subarray 문제는 합 리스트를 사용하는게 효율적이다.
        minValue = 0                  # 모든 리스트를 포함할 경우를 생각하여 minValue를 0으로 초기화
        exMax = - 1e9
        for i in range(len(sumList)):
            exMax = max(exMax, sumList[i] - minValue)   # minValue를 저장하여 현재 위치에 있는 숫자와의 
            if minValue > sumList[i]:
                minValue = sumList[i]
        return exMax
# https://leetcode.com/problems/maximum-subarray/submissions/
