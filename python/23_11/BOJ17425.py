import sys

inp = sys.stdin.readline

# x보다 작은 
maxV = max(n_list := [int(inp()) for _ in range(int(inp()))])
n_list.sort()
n_idx = 0
dp = [set() for _ in range(maxV + 1)]
n = 1
s = 0
while n_idx != len(n_list):
    # print(n)
    if len(dp[n]) == 0:
        dp[n].add(1)
        dp[n].add(n)
    s += sum(dp[n])
    for i in range(2, maxV + 1):
        if (tmp:=n * i) <= maxV:
            dp[tmp] = dp[n] | dp[i] | dp[tmp]
                # print(dp[tmp], tmp)
        else:
            break
    if n == n_list[n_idx]:
        print(s)
        # print(dp[:11])
        n_idx += 1
    n += 1

