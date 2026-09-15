# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        
        #preorder capturing the right boundary

        def left_boundary(node):
            if not node or (not node.left and not node.right):
                return
            result.append(node.val)
            if node.left:
                left_boundary(node.left)
            else:
                left_boundary(node.right)

        def get_leaves(node):
            if not node:
                return
            if not node.left and not node.right:  
                result.append(node.val)
                return
            get_leaves(node.left)
            get_leaves(node.right)
        
        def right_boundary(node):
            if not node or (not node.left and not node.right):
                return
            
            if node.right:
                right_boundary(node.right)
            else:
                right_boundary(node.left)

            result.append(node.val)
        
        result.append(root.val)
        if not root.left and not root.right:
            return result

        left_boundary(root.left)
        get_leaves(root)
        right_boundary(root.right)

        return result
            
        
        