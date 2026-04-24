class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        
        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or grid[r][c] == 1:
                return 0
            if (r,c) == (rows - 1, cols - 1):
                return 1
            visited.add((r,c))
            paths = 0
            for dx,dy in directions:
                x = dx + r
                y = dy + c
                paths += dfs(x,y)
            visited.remove((r,c))
            return paths

        return dfs(0,0)
        
        
        