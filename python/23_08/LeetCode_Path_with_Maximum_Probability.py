# Path with Maximum Probability

import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        q = [[-1, start_node]]
        tmp = [[] for _ in range(n)]
        for i in range(len(edges)):
            s, e = edges[i]
            tmp[s].append([e, succProb[i]])
            tmp[e].append([s, succProb[i]])
        dp = [0 for _ in range(n)]
        edges = tmp
        while q:
            c, node = heapq.heappop(q)
            if node == end_node:
                return -c
            for next_node, cost in edges[node]:
                if (tmp := -c * cost) > dp[next_node]:
                    dp[next_node] = tmp
                    heappush(q, [-tmp, next_node])
        else:
            return 0

# https://leetcode.com/problems/path-with-maximum-probability/description/