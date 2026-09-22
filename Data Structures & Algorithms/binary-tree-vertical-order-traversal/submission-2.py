# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root, 0)])

        result = []
        hashmap = collections.defaultdict(list)

        while queue:
            node, position = queue.popleft() # 0,3, 9,-1
            hashmap[position].append(node.val) # -1:[9]
            if node.left:
                queue.append((node.left,position - 1)) # 9
            if node.right:
                queue.append((node.right,position + 1)) # 9,20
                
        sorted_keys = sorted(hashmap.keys())
        for k in sorted_keys:
            result.append(hashmap[k])
        return result        
        