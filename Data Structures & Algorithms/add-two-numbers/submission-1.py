class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        # Loop continues if either list has digits left OR if there is a leftover carry (e.g. 5 + 5 = 10)
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # 1. Total sum for the current place value
            total = l1_val + l2_val + carry

            # 2. Extract carry for the next node
            carry = total // 10

            # 3. Create the node with the remainder
            curr.next = ListNode(total % 10)
            curr = curr.next

            # 4. Safely advance pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next