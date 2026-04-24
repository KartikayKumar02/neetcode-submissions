class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, temp = [],[]
        nums.sort()

        def dfs(index):
            if index == len(nums):
                result.append(temp[:])
                return
            
            
            
            temp.append(nums[index])
            dfs(index + 1)
            temp.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1)
        
        dfs(0)
        return result

        