# N번째 큰 수

import sys
import heapq
def solution():
    inp = sys.stdin.readline
    heap = []
    n = int(inp())
    for num in map(int, inp().split()):
        heapq.heappush(heap, num)

    for _ in range(n - 1):
        for num in map(int, inp().split()):
            heapq.heappush(heap, num)
            heapq.heappop(heap)
    return heap[0]

if __name__ == "__main__":
    print(solution())

# https://www.acmicpc.net/problem/2075