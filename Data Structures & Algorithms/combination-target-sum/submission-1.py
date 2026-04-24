class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, temp = [],[]

        def dfs(index,curr_sum):
            if curr_sum > target or index == len(nums):
                return
            if curr_sum == target:
                result.append(temp[:])
                return
            temp.append(nums[index])
            dfs(index,curr_sum + nums[index])
            temp.pop()
            dfs(index + 1,curr_sum)
        dfs(0,0)
        return result
        