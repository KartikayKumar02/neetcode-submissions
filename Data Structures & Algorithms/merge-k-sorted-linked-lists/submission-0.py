# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        min_heap = []

        for index,head in enumerate(lists):
            if head:
                heapq.heappush(min_heap,(head.val,index,head))
        
        # new list
        dummy = ListNode(0)
        curr = dummy 

        while min_heap:
            value,index,node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        return dummy.next

        