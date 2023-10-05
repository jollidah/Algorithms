import sys

def Solution():
    global y, x, d, res
    inp = sys.stdin.readline
    dt = ((0, -1), (1, 0), (0, 1), (-1, 0))
    pos = ((-2, 0, 0.02), (-1, 0, 0.07), (-1, 1, 0.01), (-1, -1, 0.1), (0, -2, 0.05), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02), (1, -1, 0.1))
    rotation = (
    (lambda x: (x[0], x[1], x[2])),
    (lambda x: (-x[1], x[0], x[2])),
    (lambda x: (-x[0], -x[1], x[2])),
    (lambda x: (x[1], -x[0], x[2])))
    n = int(inp())
    grid = [list(map(int, inp().split())) for _ in range(n)]
    res = 0
    d = 3
    y = n // 2
    x = y

    def progress_step():
        global y, x, d, res
        y, x = y + dt[d][0], x + dt[d][1]
        sands = grid[y][x]
        grid[y][x] = 0
        flied_sands = 0
        tmp_pos = map(rotation[d], pos)
        for dy, dx, ratio in tmp_pos:
            tmpY, tmpX = y + dy, x + dx
            tmp = int(sands * ratio)
            if tmp:
                flied_sands += tmp
                if n > tmpY >= 0 and n > tmpX >= 0:
                    grid[tmpY][tmpX] += tmp
                else:
                    res += tmp
        if n > (tmpY := y + dt[d][0]) >= 0 and n > (tmpX := x + dt[d][1]) >= 0:
            grid[tmpY][tmpX] += sands - flied_sands
        else:
            res += sands - flied_sands

    for i in range(1, n):
        for __ in range(2):
            d = (d + 1) % 4
            for _ in range(i):
                progress_step()
    d = (d + 1) % 4
    for _ in range(n - 1):
        progress_step()
    print(res)
    
if __name__ == "__main__":
    Solution()
