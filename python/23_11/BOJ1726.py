import sys
import heapq
# 이미 겹친 애 중에 1만큼 차이가 났다면, 이전에 겹친 애의 반대 방향만 탐색하면 된다.
# 둘이 같다면, 서로 온 방향의 반대 방향을 제외하고 탐색하면 된다. 
# 나머진 다익스트라 + DP (라운드 별로), DP에는 라운드 정보와 방향 정보를 저장

def Solution():
    def match_dir(d):
        if d == 1:
            return 1
        elif d == 2:
            return 3
        elif d == 3:
            return 2
        return 0

    dt = ((-1, 0), (0, 1), (1, 0), (0, -1))
    q = []
    inp = sys.stdin.readline
    m, n = map(int, inp().split())
    grid = [list(map(int, inp().split())) for _ in range(m)]
    dp = [[[1e9, 0] for _ in range(n)] for _ in range(m)]
    y, x, d = map(int, inp().split())
    y, x, d = y - 1, x - 1, match_dir(d)
    dp[y][x][0], dp[y][x][1] = 0, d
    heapq.heappush(q, [0, y, x, d])
    heapq.heappush(q, [2, y, x, (d + 2) % 4])

    targetY, targetX, targetDir = map(int, inp().split())
    targetY, targetX, targetDir = targetY - 1, targetX - 1, match_dir(targetDir)

    res = 1e9
    round = 0
    while res + 2 > round and q:
        round, y, x, d = heapq.heappop(q)
    # print(round, y, x, d)
        if y == targetY and x == targetX:
            res = min(res, round + abs(targetDir - d))
        # print("shit", round, y, x, d, targetDir)
        round += 1
        for k in (1, 2, 3):
            tmpY, tmpX = y + k * dt[d][0], x + k * dt[d][1]
            try:
                if tmpY >= 0 and tmpX >= 0 and grid[tmpY][tmpX] == 0:
                    if dp[tmpY][tmpX][0] == round and abs(dp[tmpY][tmpX][1] - d) == 1:
                        heapq.heappush(q, [round, tmpY, tmpX, d])
                    elif dp[tmpY][tmpX][0] > round:
                        dp[tmpY][tmpX][0], dp[tmpY][tmpX][1] = round, d
                        heapq.heappush(q, [round, tmpY, tmpX, d])
                else:
                    break
            except IndexError:
                break
        if round - 1 == dp[y][x][0]:
            for add in (1, 3):
                tmpD = (d + add) % 4
                heapq.heappush(q, [round, y, x, tmpD]) 

    print(res)
if __name__ == "__main__":
    Solution()
