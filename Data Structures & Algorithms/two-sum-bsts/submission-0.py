# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        temp1 = set()
        temp2 = set()

        def dfs(node,res):
            if not node:
                return
            dfs(node.left,res)
            res.add(node.val)
            dfs(node.right,res)
        dfs(root1,temp1)
        dfs(root2,temp2)
        for val in temp1:
            newTarget = target - val
            if newTarget in temp2:
                return True
        return False