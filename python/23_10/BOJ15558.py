# 점프 게임
import sys

def Solution():
    inp = sys.stdin.readline

    n, k = map(int, inp().split())
    if n == 1:
        print(1)
        exit(0)
    r =[inp().strip() for _ in range(2)]
    visit = [[False for _ in range(n)] for _ in range(2)]

    next = [(0, 0)]
    visit[0][0] = True
    for round in range(n):
        tmp = set()
        for i, idx in next:
            for line, jump in (i, idx + 1), (i, idx - 1), (1 - i, idx + k):
                try:
                    if jump > round and r[line][jump] == "1" and not visit[line][jump]:
                        visit[line][jump] = True
                        tmp.add((line, jump))
                except:
                    print(1)
                    return 
        if not tmp:
            break
        next = list(tmp)
    print(0)

if __name__ == "__main__":
    Solution()

# https://www.acmicpc.net/problem/15558