from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!= n - 1:
            return False
        adjacency_list = {}
        
        for node1,node2 in edges:
            if node1 in adjacency_list:
                adjacency_list[node1].append(node2)
            else:
                adjacency_list[node1] = [node2]
            if node2 in adjacency_list:
                adjacency_list[node2].append(node1)
            else:
                adjacency_list[node2] = [node1]
        queue = deque([0])
        visited = set()
        visited.add(0)


        while queue:
            node = queue.popleft()
            for neighbor in adjacency_list.get(node,[]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return True if len(visited) == n else False
        


        
        

        