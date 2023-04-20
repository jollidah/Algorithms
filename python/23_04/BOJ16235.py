import sys
from collections import deque

dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

# n : 땅의 크기, m : 초기 나무 좌표 및 위치, k : 햇수
n, m, k = map(int, input().split())

soil = [[5]*n for _ in range(n)]

# S2D2
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# 나무와, 그 나이 기록
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age)


# 봄, 여름
# 양분 먹음 / 양분없으면 -> 죽음 -> (죽은 나무) 양분에 추가
def spring_summer():
    for i in range(n):
        for j in range(n):
            dead_amount = 0
            new_trees = deque()
            for age in trees[i][j]:
                if soil[i][j] >= age:
                    soil[i][j] -= age
                    new_trees.append(age + 1)
                else:
                    dead_amount += (age // 2)
            trees[i][j] = new_trees
            soil[i][j] += dead_amount


# 가을, 겨울
# 번식 / S2D2가 각 땅에 양분 추가
def fall_winter():
    tmp_trees = [] # r, c
    for i in range(n):
        for j in range(n):
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for direction in range(8):
                        nx, ny = i + dx[direction], j + dy[direction]
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        tmp_trees.append((nx, ny))

            # 로봇이 양분추가
            soil[i][j] += A[i][j]

    for tree_position in tmp_trees:
        r, c = tree_position
        trees[r][c].appendleft(1)


for i in range(k):
    spring_summer()
    fall_winter()


cnt = 0

# 나무 수 체크
for i in range(n):
    for j in range(n):
        for k in range(len(trees[i][j])):
            cnt += 1

print(cnt)