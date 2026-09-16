class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        # (time, row, col)
        min_heap = [(grid[0][0],0,0)]
        visited = set()
        visited.add((0,0))

        n = len(grid)

        while min_heap:
            current_time, r, c = heapq.heappop(min_heap)

            if r == n - 1 and c == n - 1:
                return current_time
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Gatekeeper: Within bounds and not visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The Time Math: We take the max of our current wait time, 
                    # or the elevation of the new tile.
                    next_time = max(current_time, grid[nr][nc])
                    
                    # Add to the VIP line!
                    heapq.heappush(min_heap, (next_time, nr, nc))
            



        
        