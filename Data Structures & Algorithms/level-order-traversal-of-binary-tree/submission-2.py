from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque([root]) #1

        while queue:
            levelSize = len(queue) #1.  #2 
            temp = []

            for i in range(levelSize):
                element = queue.popleft() #1 #2 #3
                temp.append(element.val) #1 #2 #3
                if element.left:
                    queue.append(element.left) #2 #4 #6
                if element.right:
                    queue.append(element.right) #3 #5 #7
            result.append(temp) #[1],[2,3]
        return result