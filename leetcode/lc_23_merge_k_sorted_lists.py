import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Add enumeration in the tuple for dealing with equal val
        lists = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(lists)

        cur_node = root = ListNode()

        while lists:
            _, i, next_node = heapq.heappop(lists)
            cur_node.next = next_node

            cur_node = cur_node.next

            if next_node := cur_node.next:
                heapq.heappush(lists, (next_node.val, i, next_node))

        return root.next
