class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return 
        result,temp = [],[]
        def dfs(index,sums,temp,result):
            if sums == target:
                result.append(temp[:])
                return
            if index >= len(nums) or sums > target:
                return
            temp.append(nums[index])
            dfs(index,sums + nums[index],temp,result)
            temp.pop()
            dfs(index + 1,sums,temp,result)
        sums = 0
        dfs(0,sums,temp,result)
        return result