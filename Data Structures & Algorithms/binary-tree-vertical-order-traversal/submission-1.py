from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,0)])
        hashmap = defaultdict(list)
        
        while queue:
            node,position = queue.popleft() # 3, 0 , 9,-1
            hashmap[position].append(node.val)   # 0: 3,15 , -1: 9, 1:20, 2: 7  
            if node.left:
                queue.append([node.left,position - 1])
            if node.right:
                queue.append([node.right,position + 1])
            # [[9,-1],[20,+1]]
        sorted_keys = sorted(hashmap.keys()) # -1,0,1,2
        result = []
        for k in sorted_keys:
            result.append(hashmap[k]) #[9],[3,15],[20]
        return result