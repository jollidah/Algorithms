# 기타리스트

import sys

def solution():
    inp = sys.stdin.readline

    n, s, m = map(int, inp().split())
    vList = list(map(int, inp().split()))
    dp = [set() for _ in range(2)]
    dp[0].add(s)
    idx, d = 0, 0
    for i in range(n):
            (idx, d) = (0, 1) if i % 2 == 0 else (1, -1) 
            for num in dp[idx]:
                if (tmp:=num + vList[i]) <= m:
                    dp[idx + d].add(tmp)
                if (tmp:=num - vList[i]) >= 0:
                    dp[idx + d].add(tmp)
            dp[idx].clear()
            
    return max(dp[idx + d]) if dp[idx + d] else -1

if __name__ == "__main__":
    print(solution())

# https://www.acmicpc.net/problem/1495