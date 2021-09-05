from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = ListNode()
        prev_node = root
        carry = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            carry, new_node_val = divmod(l1_val + l2_val + carry, 10)

            new_node = ListNode(val=new_node_val)
            prev_node.next = new_node

            prev_node = new_node
            l1 = l1 and l1.next
            l2 = l2 and l2.next

        if carry:
            prev_node.next = ListNode(val=1)

        return root.next
