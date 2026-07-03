# Intuition:
# We process the linked list in repeating blocks:
# 1. Keep the next m nodes.
# 2. Delete the following n nodes.
#
# A pointer (curr) is used to mark the last node that should be kept.
# Once we have kept m nodes, another pointer (temp) skips over the next
# n nodes. We then reconnect curr directly to the node after the deleted
# section. This process repeats until we reach the end of the list.
#
# Example:
# List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
# m = 2, n = 2
#
# Keep:   1 -> 2
# Delete: 3 -> 4
# Connect: 2 -> 5
#
# Keep:   5 -> 6
# Delete: 7 -> 8
#
# Final List:
# 1 -> 2 -> 5 -> 6
#
# Time Complexity: O(N)
# - Every node is visited at most once while either keeping or skipping.
#
# Space Complexity: O(1)
# - Only a few pointers are used regardless of the input size.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy
        count = 0

        while curr and curr.next:

            # Keep the next m nodes.
            if count < m:
                curr = curr.next
                count += 1

            else:
                # Start deleting the next n nodes.
                temp = curr.next
                count = 1

                # Move temp to the last node that should be deleted.
                while temp.next and count < n:
                    temp = temp.next
                    count += 1

                # Connect the kept portion to the node after the deleted block.
                curr.next = temp.next

                # Continue processing from the next remaining node.
                curr = curr.next

                # Reset count for keeping the next m nodes.
                count = 1

        return dummy.next
