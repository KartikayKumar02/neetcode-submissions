class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r,c) in visited or r < 0 or r >= rows or c >= cols or c<0 or grid[r][c] == 0:
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        def bfs():
            flips, q = 0, deque(visited)

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        x = r + dr
                        y = c + dc

                        if 0 <= x < rows and 0 <= y < cols and (x,y) not in visited:
                            if grid[x][y] == 1:
                                return flips
                            q.append((x,y))
                            visited.add((x,y))
                flips += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return bfs()
