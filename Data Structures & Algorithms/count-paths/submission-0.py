class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1,0],[0,1]]
        rows = m
        cols = n
        visited = {}


        def dfs(row,col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            
            if (row,col) in visited:
                return visited[(row,col)]

            if row == (rows - 1) and col == (cols - 1):
                return 1
            paths = 0
            for dx,dy in directions:
                x = dx + row
                y = dy + col
                paths += dfs(x,y)
            visited[(row,col)] = paths 
            return paths
        return dfs(0, 0)
        
