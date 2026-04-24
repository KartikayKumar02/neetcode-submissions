class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        stack1 = []
        stack2 = []

        while curr1:
            stack1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next

        head = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            sums = val1 + val2 + carry
            carry = sums // 10
            newNode = ListNode(sums % 10)
            newNode.next = head
            head = newNode
        
        return head