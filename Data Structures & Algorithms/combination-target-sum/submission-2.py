class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp = []
        result = []


        def dfs(i,cursum):
            if i >= len(nums) or cursum > target:
                return
            
            if cursum == target:
                result.append(temp[:])
                return
                
            
            temp.append(nums[i])
            dfs(i,cursum + nums[i])
            temp.pop()
            dfs(i + 1,cursum)
        dfs(0,0)
        return result

        