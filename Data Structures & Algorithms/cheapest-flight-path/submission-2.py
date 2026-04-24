from collections import Counter, defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjacency_list = defaultdict(list)

        for source,dest,cost in flights:
            adjacency_list[source].append([dest,cost])
        
        queue = deque([(src, 0, 0)])
        min_costs = [float('inf')] * n
        min_costs[src] = 0
        
        while queue:
            node, price, stops = queue.popleft()
            if stops > k:
                continue
            for neighbor, curr_price in adjacency_list[node]:
                nextCost = price + curr_price
                if nextCost < min_costs[neighbor]:
                    min_costs[neighbor] = nextCost
                    queue.append((neighbor, nextCost, stops + 1))
        
        return min_costs[dst] if min_costs[dst] != float('inf') else -1