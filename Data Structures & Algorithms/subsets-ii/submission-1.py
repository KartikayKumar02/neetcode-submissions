class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        nums.sort()
        def dfs(index):
            if index == len(nums):
                if temp not in result:
                    result.append(temp[:])
                return
            temp.append(nums[index])
            print(temp)
            dfs(index+1)
            temp.pop()
            dfs(index + 1)
        dfs(0)
        return result