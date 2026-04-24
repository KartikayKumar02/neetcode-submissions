class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [[1,0],[0,1],[0,-1],[-1,0]]

        self.area = 0
        maxarea = 0

        def dfs(r,c):
            if r  < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
                return

            visited.add((r,c))
            if grid[r][c] == 1:
                self.area += 1
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    self.area = 0
                    dfs(row,col)
                    maxarea = max(maxarea, self.area)
        return maxarea