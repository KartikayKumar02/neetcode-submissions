class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        temp = []
        result = []


        def dfs(temp):

            if len(temp) == len(nums):
                result.append(temp[:])


            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                # Take it: Put it in the basket
                temp.append(nums[i])
                
                # Move forward: Notice there is NO index + 1! 
                # We just call dfs to pick the next item for the basket.
                dfs(temp)
                
                # Backtrack: Take it out of the basket so we can try a different path
                temp.pop()
        dfs(temp)
        return result


        