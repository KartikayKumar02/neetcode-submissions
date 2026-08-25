class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = defaultdict(list)
        indegree = [0] * numCourses

        for course,pre in prerequisites:
            hashmap[pre].append(course)
            indegree[course] += 1
        

        queue = []
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        result = []

        while queue:
            course = queue.pop(0)
            result.append(course)
            for c in hashmap[course]:
                indegree[c] -= 1
                
                if indegree[c] == 0:
                    queue.append(c)
        return len(result) == numCourses

