from queue import Queue


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        q = Queue()
        l = len(matrix)
        layor = l
        xPtr = 0
        yPtr = 0
        while layor > 1:    # 겉에서 부터 층층이 큐에 put한 후에 get을 통해 위치를 바꿨다
            startPoint = (l - layor) // 2     # 매 반복문마다 시작점이 달라진다는 것을 주의해야 한다
            endPoint = l -1 - startPoint      # 매 반복문마다 마침점도 달라진다는 것을 주의해야 한다
            while xPtr < endPoint:
                q.put(matrix[yPtr][xPtr])
                xPtr += 1
            while yPtr < endPoint:
                q.put(matrix[yPtr][xPtr])
                yPtr += 1
            while xPtr > startPoint:
                q.put(matrix[yPtr][xPtr])
                xPtr -= 1
            while yPtr > startPoint:     # 등호 실수 조심
                q.put(matrix[yPtr][xPtr])
                yPtr -= 1
            xPtr += layor - 1
            while yPtr < endPoint:
                matrix[yPtr][xPtr] = q.get()
                yPtr += 1

            while xPtr > startPoint:
                matrix[yPtr][xPtr] = q.get()
                xPtr -= 1

            while yPtr > startPoint:  # 등호 실수 조심
                matrix[yPtr][xPtr] = q.get()
                yPtr -= 1
            while xPtr < endPoint:
                matrix[yPtr][xPtr] = q.get()
                xPtr += 1
            xPtr -= layor - 2   # x포인터와 y 포의 위치를 초기화 하고 층의 수를 2만큼 줄여야 함
            yPtr += 1
            layor -= 2
            
# https://leetcode.com/problems/rotate-image/
