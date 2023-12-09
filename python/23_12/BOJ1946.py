import sys

def Solution():
    inp = sys.stdin.readline

    for _ in range(int(inp())):
        n = int(inp())
        score_list = [n + 1] + [0 for _ in range(n)]
        for _ in range(n):
            rating1, rating2 = map(int, inp().split())
            score_list[rating2] = rating1
        minV = n + 1
        res = 0
        for r in score_list:
            if r < minV:
                res += 1
                minV = r
        print(res)

if __name__ == "__main__":
    Solution()
