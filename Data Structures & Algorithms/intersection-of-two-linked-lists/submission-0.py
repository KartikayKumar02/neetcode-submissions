# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curra = headA
        currb = headB

        result = set()

        while curra:
            result.add(curra)
            curra = curra.next

        while currb:
            if currb in result:
                return currb
            else:
                result.add(currb)
            currb = currb.next
        return 
        
        