class Solution:

    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):  # 선택한 수의 바로 오른쪽과 리스트의 오른쪽 끝에서
            left = i + 1                # 가운데로 범위를 좁혀가며 탐색 이 아이디어가 가장 중요했다
            selected = i
            right = len(nums) - 1
            if res and nums[selected] == res[-1][1]:  # 중복을 방지
                continue
            else:
                while left != right:
                    if nums[left] + nums[selected] + nums[right] == 0:
                        res.append([nums[left], nums[selected], nums[right]])
                        print("Accepted")
                        pivot = nums[right]
                        while left != right and nums[right] == pivot: # 중복 방지 & 시간 절약
                            right -= 1
                    elif nums[left] + nums[selected] + nums[right] < 0:
                        pivot = nums[left]
                        while left != right and pivot == nums[left]: # 중복 방지 & 시간 절약
                            left += 1
                    else:
                        pivot = nums[right]
                        while left != right and pivot == nums[right]:
                            right -= 1
        return res
