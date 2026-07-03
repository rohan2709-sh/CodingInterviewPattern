# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Intuition:
-----------
Since the linked list is already sorted, all duplicate values appear
next to each other. Instead of removing duplicates one by one, we can
skip an entire block of duplicate nodes in a single step.

For every node:
1. Compare it with the next node.
2. If their values are different, simply move forward.
3. If they are the same, keep advancing a temporary pointer until
   a different value is found.
4. Connect the current node directly to this first different node,
   effectively removing all duplicate nodes in between.

Example:
---------
Input:
1 -> 1 -> 1 -> 2 -> 3 -> 3

Step 1:
curr = 1
temp moves: 1 -> 1 -> 2
Reconnect:
1 -> 2 -> 3 -> 3

Step 2:
curr = 2
No duplicate, move ahead.

Step 3:
curr = 3
temp moves: 3 -> None
Reconnect:
1 -> 2 -> 3

Output:
1 -> 2 -> 3

Time Complexity:
----------------
O(n)
Each node is visited at most once by either curr or temp.

Space Complexity:
-----------------
O(1)
Only a few pointers are used, so no extra space proportional to the
input size is required.
"""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Start traversing from the head of the linked list
        curr = head

        # Continue until there is no next node to compare
        while curr and curr.next:

            # If the current node and next node have the same value,
            # we have found duplicate(s)
            if curr.val == curr.next.val:

                # Temporary pointer to skip all duplicate nodes
                temp = curr.next

                # Move temp until a different value is found
                while temp and temp.val == curr.val:
                    temp = temp.next

                # Connect current node to the first non-duplicate node
                curr.next = temp

            # Move to the next unique node
            curr = curr.next

        return head
