class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, temp = set(), []
        
        def dfs(sums,temp,result,index):
            if sums == target:
                result.add(tuple(temp))
                return
            
            if index == len(candidates) or sums > target:
                return

            temp.append(candidates[index])
            dfs(sums + candidates[index],temp,result,index + 1)
            temp.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(sums,temp,result,index + 1)
        
        dfs(0,temp,result,0)
        return [list(x) for x in result]