class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        visited = collections.defaultdict(int)

        left, right = 0,0
        maxfruits = 0

        while right < len(fruits):
            visited[fruits[right]] += 1 #0:1,1:1,2:1

            while len(visited) > 2:
                visited[fruits[left]] -= 1
                if visited[fruits[left]] == 0:
                    del visited[fruits[left]]
                left += 1
            
            maxfruits = max(maxfruits, right - left + 1)
            right += 1
        return maxfruits