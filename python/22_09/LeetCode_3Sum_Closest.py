class Solution:

    def threeSumClosest(self, nums, target):
        nums.sort()
        lastSelected = 1e9    # 초기 최솟값을 매우 큰 값으로 초기화
        minValue = 1e9
        minAbs = 1e9
        for i in range(len(nums) - 2):
            if lastSelected == nums[i]:   # 중복 바지 -> 시간 효율 up
                continue
            else:
                left = i + 1
                selected = i
                right = len(nums) - 1
                lastSelected = nums[i]
                while left != right:
                    sumNums = nums[left] + nums[selected] + nums[right]   # 합을 변수로 저장하여 연산 수를 줄였어야 함
                    if sumNums == target:
                        return target
                    if abs(sumNums - target) < minAbs:
                        minAbs = abs(sumNums - target)
                        minValue = sumNums
                    if sumNums < target:
                        pivot = nums[left]
                        while left != right and pivot == nums[left]:  # 중복 방지 -> 시간 효율 up
                            left += 1
                    else:
                        pivot = nums[right]
                        while left != right and pivot == nums[right]:
                            right -= 1
        return minValue
