# Single-Threaded CPU

import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        stage = []
        t = 0
        for i in range(len(tasks)):
            tasks[i].append(i)
        heapq.heapify(tasks)
        while tasks or stage:
            if not stage and t < tasks[0][0]:
                t = tasks[0][0]
            while tasks and tasks[0][0] <= t:
                heapq.heappush(stage, [tasks[0][1], tasks[0][2]])
                heapq.heappop(tasks)
            pTime, idx = heapq.heappop(stage)
            t += pTime
            res.append(idx)
        return res

# https://leetcode.com/problems/single-threaded-cpu/description/
