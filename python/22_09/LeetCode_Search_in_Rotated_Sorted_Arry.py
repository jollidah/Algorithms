class Solution:

    def search(self, nums, target: int) -> int:     # 투포인터를 이용
        l = len(nums)           # 리스트의 길이를 저장할 변수
        left = 0                # 좌측 포인터
        right = len(nums) - 1   # 우측 포인터
        if nums[left] <= target:    # 좌측 포인터가 target보다 작다면
            while True:
                if nums[left] == target:    # 포인터와 target이 같은지 확인
                    return left
                if left + 1 >= l:           # 포인터와 다음 포인터 위치가 리스트 내에 있는지 확인
                    return - 1
                elif nums[left] > nums[left + 1]:   # 다음 포인터가 현재 포인터보다 작다면 피봇을 만난 것이므로 -1 리턴
                    return -1
                left += 1
        else:                       # 우측 포인터도 같은 방법으로 확인
            while True:
                if nums[right] == target:
                    return right
                if right - 1 <= 0:
                    return -1
                if nums[right] < nums[right - 1]:
                    return -1
                right -= 1
                
# https://leetcode.com/problems/search-in-rotated-sorted-array/
