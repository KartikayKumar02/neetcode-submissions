# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        self.serialized_string = ""
        def dfs(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        self.serialized_string = ",".join(result)
        return self.serialized_string
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")

        def dfs(node_list):
            val = node_list.pop(0)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs(node_list)
            node.right = dfs(node_list)
            return node
        return dfs(vals)
        
        

            
