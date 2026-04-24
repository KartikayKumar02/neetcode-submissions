from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        visited = set()
        queue = deque()

        # 1. Add all Treasure Chests (0) to the queue initially
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        # 2. Define Directions: [Down, Up, Right, Left]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 3. BFS Traversal
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # Loop through all 4 directions
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Check if the new coordinate is:
                    # a. In bounds
                    # b. Not a wall (-1)
                    # c. Not already visited
                    if (row in range(rows) and 
                        col in range(cols) and 
                        grid[row][col] != -1 and 
                        (row, col) not in visited):
                        
                        # Update the distance and add to queue
                        grid[row][col] = grid[r][c] + 1
                        visited.add((row, col))
                        queue.append((row, col))