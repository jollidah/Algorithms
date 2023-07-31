import sys
import heapq

def soluiton():
    inp = sys.stdin.readline
    n = int(inp())
    h = []
    candidates = []
    for _ in range(n):
        p, d = map(int, inp().split())
        heapq.heappush(h, [-d, -p])
    day = 0
    res = 0
    while h:
        day += 1
        if not candidates:
            day = h[0][0]       
        while h and day == h[0][0]:
            heapq.heappush(candidates, heapq.heappop(h)[1])
        res -= heapq.heappop(candidates)

    while candidates and day != -1:
        day += 1
        res -= heapq.heappop(candidates)
    return res


# def solution():
#     import sys
#     import heapq

#     n = int(sys.stdin.readline())
#     lecture = [list(map(int, sys.stdin.readline().split()))  for i in range(n)]

#     lecture.sort(key=lambda x: x[1])

#     heap = []

#     for pay, day in lecture:
#         heapq.heappush(heap, pay)

#         if day < len(heap):
#             heapq.heappop(heap)
#     print(sum(heap))

if __name__ == "__main__":
    print(soluiton())