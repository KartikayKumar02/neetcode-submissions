class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in cache:
                return cache[i]

            # choose current and skip
            current = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            cache[i] = max(current,skip)
            return cache[i]
        return dfs(0)
        