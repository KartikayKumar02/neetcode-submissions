class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_brackets = 0
        closed_brackets = 0
        result = []
        def dfs(openb,closeb,path):
            if openb == closeb == n:
                result.append(path)
                return
            if openb < n:
                dfs(openb + 1,closeb,path + '(')
            if closeb < openb:
                dfs(openb,closeb+1,path + ')')
        dfs(open_brackets,closed_brackets,'')
        return result