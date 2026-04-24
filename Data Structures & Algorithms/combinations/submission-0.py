class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result,temp = [], []
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        def dfs(index):
            if len(temp) == k:
                result.append(temp[:])
                return
            if index == len(nums):
                return
            temp.append(nums[index])
            dfs(index + 1)
            temp.pop()
            dfs(index + 1)
        
        dfs(0)
        return result
            