class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder -> left -> root -> right
        # postorder: left -> right -> root
        if not inorder or not postorder:
            return 
        root_val = postorder[-1]
        node = TreeNode(root_val)
        inorderRootIndex = inorder.index(root_val)
        node.left = self.buildTree(inorder[:inorderRootIndex],postorder[:inorderRootIndex])
        node.right = self.buildTree(inorder[inorderRootIndex + 1: ],postorder[inorderRootIndex: - 1])
        return node