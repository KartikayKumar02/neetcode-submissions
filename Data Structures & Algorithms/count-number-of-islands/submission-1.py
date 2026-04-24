class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        islands = 0

        def dfs(r,c):
            if r  < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == '0':
                return

            visited.add((r,c))
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    islands += 1
        return islands






        