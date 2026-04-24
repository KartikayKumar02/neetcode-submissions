
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)
        indegree = [0] * numCourses
        
        for course,precourse in prerequisites:
            adjacencyList[precourse].append(course)
            indegree[course] += 1
        q = deque()
        for course_id,degree in enumerate(indegree):
            if degree == 0:
                q.append(course_id)
        

        path = []

        while q:
            node = q.popleft()
            path.append(node)

            for neighbor in adjacencyList[node]:
                if indegree[neighbor] > 0:
                    indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return path if numCourses == len(path) else []

        



        