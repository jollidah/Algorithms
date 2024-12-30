import sys

def solution():
    inp = sys.stdin.readline
 
    n = int(inp())
    dp = [float('inf')] * 101
    dp[2] = 1
    dp[3] = 7
    dp[4] = 4
    dp[5] = 2
    dp[6] = 6
    dp[7] = 8
    dp[8] = 10

    for num in range(9,101):
        for i in range(2,8):
            if i != 6:
                dp[num] = min(dp[num], dp[num - i] * 10 + dp[i])
            else:
                dp[num] = min(dp[num], dp[num - i] * 10)
    for _ in range(n):
        k = int(inp())
        max_value = ('7' if k % 2 else '1' ) + '1' *(k // 2 - 1)
        print(dp[k],max_value)

if __name__ == "__main__":
    solution()
