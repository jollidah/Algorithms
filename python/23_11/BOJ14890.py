# 경사로

n, l = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def check_line(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or step[i + j]:
                    return False
                if line[i] == line[i + j]:
                    step[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or step[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    step[i - j - 1] = True
    return True


for i in range(n):
    step = [False] * n
    if check_line([grid[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    step = [False] * n
    if check_line([grid[i][j] for i in range(n)]):
        ans += 1

print(ans)

# https://www.acmicpc.net/problem/14890