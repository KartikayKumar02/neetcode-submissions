class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []


        def dfs(temp):
            if len(temp) == len(nums):
                result.append(temp[:])
                
            
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(temp)
                temp.pop()
        dfs([])
        return result
            