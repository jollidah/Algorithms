import sys
from collections import deque

def Solution():
    water_copy = ((-1, -1), (-1, 1), (1, 1), (1, -1))
    dt = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    inp = sys.stdin.readline

    n, m = map(int, inp().split())
    water = [list(map(int, inp().split())) for _ in range(n)]
    # 구름 초기화
    clouds = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])

    for _ in range(m):
        # 구름 이동 물의 양 증가
        d, s = map(int, inp().split())
        moved_clouds = set()
        while clouds:
            y, x = clouds.popleft()
            dy, dx = dt[d - 1]
            ty, tx = (y + s * dy) % n, (x + s * dx) % n
            water[ty][tx] += 1
            moved_clouds.add((ty, tx))
        # 물 복사
        for y, x in moved_clouds:
            cnt = 0
            for dy, dx in water_copy:
                ty, tx = y + dy, x + dx
                if n > ty >= 0 and n > tx >= 0 and water[ty][tx] != 0:
                    cnt += 1
            water[y][x] += cnt
        next = deque()
        # 다음 구름
        for y in range(n):
            for x in range(n):
                if (y, x) not in moved_clouds and water[y][x] >= 2:
                    water[y][x] -= 2
                    next.append((y, x))
        clouds = next

    print(sum(map(sum, water)))

if __name__ == "__main__":
    Solution()
