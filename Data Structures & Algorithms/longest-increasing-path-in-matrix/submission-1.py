class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}


        maxlen = 0

        def dfs(r,c,prev_val):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev_val:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            current_val = matrix[r][c]

            down = dfs(r+1,c,current_val)
            right = dfs(r,c+1,current_val)
            up = dfs(r-1,c,current_val)
            left = dfs(r,c-1,current_val)

            cache[(r, c)] = 1 + max(up, down, left, right)
            return cache[(r, c)]
        

        for row in range(rows):
            for col in range(cols):
                maxlen = max(maxlen,dfs(row,col,float('-inf')))
        return maxlen

        