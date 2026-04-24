# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = []

        def height(node):
            if not node:
                return -1
            
            left = height(node.left)
            right = height(node.right)

            current_height = 1 + max(left,right)
            if len(self.result) == current_height:
                self.result.append([])

            self.result[current_height].append(node.val)
            return current_height
        
        height(root)
        return self.result
        