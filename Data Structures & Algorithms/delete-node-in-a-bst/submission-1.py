# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return
        
        def dfs(node,key):
            if not node:
                return None
            
            # searching for the node
            if key > node.val:
                node.right = dfs(node.right,key)
            elif key < node.val:
                node.left = dfs(node.left,key)
            else:
                # Node found
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                
                # both children exist
                curr = node.right
                while curr.left:
                    curr = curr.left
                node.val = curr.val

                # delete successor from right subtree
                node.right = dfs(node.right, node.val)
            return node
        return dfs(root,key)