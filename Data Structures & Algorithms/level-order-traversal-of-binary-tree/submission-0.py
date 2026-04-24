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

        queue = deque([root])
        while queue:
            levelSize = len(queue)
            temp = []  # Initialize temp list here

            for i in range(levelSize):
                element = queue.popleft()  # Pop from the front of the deque
                temp.append(element.val)   # Append the value of the node

                if element.left:
                    queue.append(element.left)  # Append left child to the queue
                if element.right:
                    queue.append(element.right)  # Append right child to the queue

            result.append(temp)
        return result
