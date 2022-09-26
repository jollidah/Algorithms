class Solution:
    def trap(self, height) -> int:
        res = 0
        maxHeight = 0      # 기준이 될 높이(최고값)
        leftPtr = 0
        rightPtr = len(height) - 1
        while leftPtr < rightPtr:
            while height[leftPtr] <= maxHeight and leftPtr < rightPtr:    # 기준보다 더 높은 높이의 벽을 만난 경우 반복문 종료
                res += maxHeight - height[leftPtr]                        # 결과값에 현재까지 저장되어 있는 빗물을 더함
                leftPtr += 1                                              # 왼쪽 포인터 이동
            while height[rightPtr] <= maxHeight and leftPtr < rightPtr:   
                res += maxHeight - height[rightPtr]
                rightPtr -= 1
            maxHeight = min(height[leftPtr], height[rightPtr])            # 왼쪽과 오른쪽 포인터가 지정하고 있는 값중에 더 낮은 것을 최대 높이로 지정
        return res
      
  # https://leetcode.com/problems/trapping-rain-water/submissions/
