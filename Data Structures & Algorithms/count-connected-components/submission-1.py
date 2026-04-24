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
        # queue = deque()
        stack = []
        components = 0

        for node in range(n):
            stack.append(node)
            if node not in visited:
                stack.append(node)
                while stack:
                    current_node = stack.pop()
                    for neighbor in adjacency_list.get(current_node,[]):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                components += 1
        return components





        