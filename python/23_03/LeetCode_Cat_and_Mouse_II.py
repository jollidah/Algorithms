#  Cat and Mouse II

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        mouse_pos, cat_pos = None, None
        available = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '#':
                    available += 1
                if grid[i][j] == 'M':
                    mouse_pos = (i, j)
                elif grid[i][j] == 'C':
                    cat_pos = (i, j)

        @functools.lru_cache(None)
        def dp(turns, cp, mp):
            # print(turns, cp ,mp)

            if turns == 2 * available:
                return False
            
            if cp == mp:
                return False

            # cat
            if turns % 2 == 1:
                for dx, dy in dirs:
                    for i in range(catJump + 1):
                        cy = cp[0] + dy * i
                        cx = cp[1] + dx * i
                        if m > cy >= 0 and n > cx >= 0 and grid[cy][cx] != "#":
                            if not dp(turns + 1, (cy, cx), mp) or grid[cy][cx] == "F":
                                return False
                        else:
                            break
                return True
            # mouse
            else:
                for dx, dy in dirs:
                    for i in range(mouseJump + 1):
                        my = mp[0] + dy * i
                        mx = mp[1] + dx * i
                        if m > my >= 0 and n > mx >= 0 and grid[my][mx] != "#":
                            if dp(turns + 1, cp, (my, mx)) or grid[my][mx] == "F":
                                return True
                        else:
                            break
                return False
        
        return dp(0, cat_pos, mouse_pos)


# https://leetcode.com/problems/cat-and-mouse-ii/description/
