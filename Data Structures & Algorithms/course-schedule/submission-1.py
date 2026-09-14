class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if not prerequisites:
            return True
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        for course,prerequisite in prerequisites:
            adjList[prerequisite].append(course)
            indegree[course] += 1


        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        result = []
        while queue:
            course = queue.pop(0)
            result.append(course)
            for c in adjList[course]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
        return len(result) == numCourses

                
            
            
        

