from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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

        visited = set()
        queue = deque()
        components = 0

        for node in range(n):
            print(node)
            if node not in visited:
                queue.append(node)
                while queue:
                    current_node = queue.popleft()
                    for neighbor in adjacency_list.get(current_node,[]):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                components += 1
        return components





        