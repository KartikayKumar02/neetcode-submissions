# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        self.maxlength = 0
        def dfs(node,parent,length):
            if node is None:
                return
            if node and parent and node.val == parent.val + 1:
                length += 1
            else:
                length = 1
            self.maxlength = max(self.maxlength,length)
            dfs(node.left,node,length)
            dfs(node.right,node,length)     
        dfs(root,None,0)    
        return self.maxlength   