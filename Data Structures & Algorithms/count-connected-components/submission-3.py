class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        stack = []
        adjList = collections.defaultdict(list)
        visited = set()

        for edge1,edge2 in edges:
            adjList[edge1].append(edge2)
            adjList[edge2].append(edge1)

        # {0:1,1:[2,0],3:4}

        queue = deque()
        components = 0

        for i in range(n):
            if i not in visited:
                queue.append(i)

                while queue:
                    node = queue.popleft()

                    for i in adjList[node]:
                        if i not in visited:
                            visited.add(i)
                            queue.append(i)
                components += 1
        return components




        


