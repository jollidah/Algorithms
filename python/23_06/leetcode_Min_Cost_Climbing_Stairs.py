from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_count = len(cost)
        min_cost = [0] * (total_count+1)
        
        for i in range(2, total_count + 1):
            one_step = min_cost[i-1] + cost[i-1]
            two_step = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[total_count]
