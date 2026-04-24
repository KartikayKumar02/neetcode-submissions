class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, temp = [],[]
        candidates.sort()

        def dfs(index,curr_sum):
            if curr_sum == target:
                result.append(temp[:])
                return
            if curr_sum > target or index == len(candidates):
                return
            
            temp.append(candidates[index])
            dfs(index + 1,curr_sum + candidates[index])
            temp.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1,curr_sum)
        dfs(0,0)
        return result
        