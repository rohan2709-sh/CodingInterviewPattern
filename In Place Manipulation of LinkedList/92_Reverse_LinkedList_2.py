# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# ============================================================
# INTUITION & EXPLANATION
# ============================================================
# We need to reverse only a portion of the list (from position
# 'left' to position 'right'), while keeping the rest of the
# list connected in its original order.
#
# Strategy: break the problem into 3 conceptual parts:
#   [ before ]  ->  [ middle: left...right ]  ->  [ after ]
#
# Steps:
#   1. Use a dummy node before 'head' so we don't need special
#      handling when left == 1 (i.e., no "before" part).
#   2. Walk forward counting nodes until we reach position 'left'.
#      - 'left_portion' = node just BEFORE position 'left'
#        (this will connect to the new head of the reversed part)
#      - 'middle_portion' = node AT position 'left'
#        (this will become the TAIL after reversal)
#   3. Continue walking until we reach position 'right'.
#      - 'right_portion' = node just AFTER position 'right'
#        (the untouched remainder of the list)
#      - Cut the link between 'right' node and 'right_portion' so
#        the middle segment is fully isolated. This makes it safe
#        to reverse without disturbing the rest of the list.
#   4. Reverse the isolated middle segment using the standard
#      iterative reversal technique (prev/curr/temp pointers).
#   5. Reconnect the pieces:
#      - left_portion.next -> new head of reversed segment
#      - walk to the end of the reversed segment (old 'middle_portion'
#        node, now the tail) and point it to 'right_portion'
#   6. Return dummy.next, which is the (possibly unchanged) head.
#
# Time Complexity:  O(n) — one pass to locate + one pass to reverse
# Space Complexity: O(1) — reversal done in place, only pointers used
# ============================================================

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        count = 0
        left_portion = None

        # Move curr forward until it lands on the node at position 'left'.
        # Along the way, left_portion tracks the node just before it
        # (or dummy, if left == 1) — this is our reconnection anchor.
        while count < left:
            left_portion = curr
            curr = curr.next
            count += 1
        middle_portion = curr  # node at position 'left'; becomes tail after reversal

        # Keep moving curr forward until it lands on the node at position 'right'.
        while count < right:
            curr = curr.next
            count += 1
        right_portion = curr.next  # node just after 'right' — untouched remainder
        curr.next = None           # detach the middle segment [left..right] completely

        # Reverse the now-isolated middle segment.
        reversed_node = self.reverse(middle_portion)

        # Reconnect the "before" part to the new head of the reversed segment.
        left_portion.next = reversed_node
        temp = left_portion

        # Walk to the end of the reversed segment (its new tail)
        # so we can reconnect it to the "after" part.
        while temp.next:
            temp = temp.next
        temp.next = right_portion  # stitch reversed segment's tail -> remainder of list

        return dummy.next

    def reverse(self, head):
        # Standard iterative in-place reversal:
        # repeatedly flip each node's 'next' pointer to point backward.
        curr = head
        prev = None
        while curr:
            temp = curr.next   # save the next node before we overwrite curr.next
            curr.next = prev   # reverse the pointer direction
            prev = curr        # advance prev to current node
            curr = temp         # advance curr to the saved next node
        return prev  # prev is now the new head of the reversed list
