class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        temp,result = [],[]

        def backtrack(index,temp,result):
            if index == len(nums):
                result.append(temp[:])
                return
            
            temp.append(nums[index])
            backtrack(index + 1, temp,result)
            temp.pop()
            backtrack(index + 1, temp,result)
        
        backtrack(0,temp,result)
        return result
        