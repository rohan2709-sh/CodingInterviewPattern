# Time Complexity: O(L) — single pass through the list of length L
# Space Complexity: O(1) — only two pointers used, no extra data structures

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Move 'right' exactly n steps ahead of the start.
        # This creates a gap of n between 'right' and where 'left' will begin.
        right = head
        index = 0
        while index < n:
            right = right.next
            index += 1

        # KEY INSIGHT:
        # If 'right' is None after n steps, the gap spans the whole list —
        # meaning the node to remove is the head itself.
        # Return head.next to skip it.
        if right == None:
            return head.next

        # Start 'left' at head and advance both pointers together
        # until 'right' reaches the last node (right.next == None).
        # Because the gap is n, 'left' will stop exactly one node
        # before the target node.
        left = head
        while right.next != None:
            right = right.next
            left = left.next

        # Skip over the target node by pointing left.next
        # to the node after it.
        left.next = left.next.next

        return head
