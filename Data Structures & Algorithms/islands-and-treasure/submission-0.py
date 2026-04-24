from typing import List
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        if not grid:
            return  # No need to return -1; returning None suffices for in-place modification
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()

        # Helper function to add a cell to the queue if it is valid
        def addCell(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            queue.append((r, c))

        # Initialize queue with all cells containing '0' and mark them as visited
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        dist = 0
        # Perform BFS to propagate distances
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                # Add neighbors
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1  # Increment distance at each BFS level
