def solution():
    import sys
    from collections import deque 

    inp = sys.stdin.readline
    s, n, k, r1, r2, c1, c2 = map(int, inp().split())
    grid = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    
    q = deque()
    q.append([0, 0, pow(n, s), k * pow(n, s - 1)])
    tmpN, tmpK = n, k
    next_n, next_k = tmpN * n, tmpK * n
    for _ in range(s):
        start = (tmpN - tmpK) // 2 
        end = start + tmpK  # 포함되지 않는 범위
        next_start, next_end = start * n, end * n
        for y in range(r1, r2 + 1):
            if start <= y % tmpN < end :
                for x in range(c1, c2 + 1):
                    if start <= x % tmpN < end and \
                        not (next_start <= x % next_n < next_end and next_start <= y % next_n < next_end):
                        grid[y - r1][x - c1] = 1
        tmpN = next_n
        tmpK = next_k
        next_n *= n
        next_k *= n
    for y in range(len(grid)):
        for e in grid[y]:
            print(e, end = "")
        print()


if __name__ == "__main__":
    solution()
