class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        islands = 0


        def dfs(row,col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0' or (row,col) in visited:
                return 

            visited.add((row,col))

            for dx,dy in directions:
                x = dx + row
                y = dy + col
                dfs(x,y)



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    islands += 1
        
        return islands

        