import sys
inp = sys.stdin.readline

def Solution(inp):
    n, m = map(int, inp().split())
    friends = [[] for _ in range(n + 1)]
    match = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, inp().split())
        friends[a].append(b)
        friends[b].append(a)

    res = 1e9

    for i in range(1, n - 1):
        for f in friends[i]:
            match[f] += 1
        for t in range(i + 1, n):
            if match[t] == 1:
                for f in friends[t]:
                    match[f] += 1
                for j in range(t + 1, n + 1):
                    if match[j] == 2:
                        res = min(res, len(friends[i]) + len(friends[t]) + len(friends[j]) - 6)
                for f in friends[t]:
                    match[f] -= 1
        for f in friends[i]:
            match[f] -= 1
    return res if res != 1e9 else -1

if __name__ == "__main__":
    print(Solution(inp))

