class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                perimeter += self.getSides(grid, row, col)
        return perimeter
    
    
    def getSides(self, grid: List[List[int]], row: int, col: int) -> int:
        sides = 0
        if grid[row][col] == 1:
            sides += self.isWater(grid, row, col - 1) + self.isWater(grid, row - 1, col) + self.isWater(grid, row, col + 1) + self.isWater(grid, row + 1, col)
        return sides
    
    
    def isWater(self, grid: List[List[int]], row: int, col: int) -> int:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if grid[row][col] == 1:
                return 0
        return 1
