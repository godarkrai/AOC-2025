with open( 'Day4Input.txt' ) as f:
    input = f.read().splitlines()

grid = []

for i in input:
    grid.append(list(i))

class Solution:

    def __init__(self, grid: list):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def getNearbyPaperRolls( self, row:int, col:int ) -> int:
        paper_rolls = 0
        directions = [(-1,0), (-1,1), (0,1), (1,1), (1, 0), (1,-1), (0,-1), (-1,-1)]
        for newX, newY in directions:
            if 0 <= row + newX < self.rows and 0 <= col + newY < self.cols:
                if self.grid[row+newX][col+newY] == '@':
                    paper_rolls += 1
        return paper_rolls
    
    def part1(self):
        paper_rolls_accessed = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == '@' and self.getNearbyPaperRolls(row,col) < 4:
                    paper_rolls_accessed += 1
        return paper_rolls_accessed
    
    def part2(self):
        total_paper_rolls = 0
        while True:
            paper_rolls_accessed = 0
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.grid[row][col] == '@' and self.getNearbyPaperRolls( row, col ) < 4:
                        paper_rolls_accessed += 1
                        self.grid[row][col] = 'x'
            if paper_rolls_accessed == 0:
                break
            total_paper_rolls += paper_rolls_accessed
        return total_paper_rolls


solution = Solution(grid)
print( "Part 1:", solution.part1() ) 
print( "Part 2:", solution.part2() ) 
# Part 1: 1569
# Part 2: 9280