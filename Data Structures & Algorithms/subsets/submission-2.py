class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, temp = [],[]

        def dfs(index):
            if index == len(nums):
                result.append(temp[:])
                return
            temp.append(nums[index])
            dfs(index + 1)
            temp.pop()
            dfs(index + 1)
        dfs(0)
        return result

        