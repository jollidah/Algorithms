class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(reverse=True)  # 이렇게 리스트가 중간중간 지워지는 경우에는 리스트를 뒤집고 기준을 while문 기준을 0으로 잡는게 좋다
        ptr = len(intervals) - 1
        while ptr > 0:
            if intervals[ptr - 1][0] <= intervals[ptr][1]:    
                if intervals[ptr][1] < intervals[ptr - 1][1]:
                    intervals.insert(ptr + 1, [intervals[ptr][0], intervals[ptr - 1][1]]) 
                    intervals.pop(ptr - 1)
                    intervals.pop(ptr - 1)
                else:
                    intervals.pop(ptr - 1)
            ptr -= 1
        return intervals[::-1]
# https://leetcode.com/problems/merge-intervals/submissions/
