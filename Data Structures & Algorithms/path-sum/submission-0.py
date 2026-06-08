# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node,sums):
            

            if not node:
                return False
            sums += node.val
            if not node.left and not node.right:
                if sums == targetSum:
                    return True
                
            return dfs(node.left,sums) or dfs(node.right,sums)

        return dfs(root,0)

        
        