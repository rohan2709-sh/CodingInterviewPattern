# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
------------------------------------ INTUITION ------------------------------------

The idea is to maintain two pointers:

1. prev
   - Points to the last node that should remain in the final list.

2. curr
   - Traverses every node in the linked list.

Whenever we encounter a node whose value equals 'val',
we don't immediately reconnect the list. Instead, we skip
all consecutive nodes having that value.

Once we reach the first node that should be kept (or None),
we connect prev.next directly to that node.

Using a dummy node makes removing the head node(s) simple,
since every node—including the original head—has a previous node.

------------------------------------ EXPLANATION ------------------------------------

Example:
head = [1,2,6,3,4,5,6], val = 6

Initial:
dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6

Step 1:
curr = 1
Not equal to 6
Move both pointers.

prev = 1
curr = 2

Step 2:
curr = 2
Not equal to 6

prev = 2
curr = 6

Step 3:
curr = 6
Found target value.

Skip all consecutive 6's:
curr moves from first 6 -> 3

Reconnect:
prev.next = 3

List becomes:
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

Step 4:
Continue traversal.

Eventually:
curr = last 6

Skip it:
curr = None

Reconnect:
prev.next = None

Final list:
1 -> 2 -> 3 -> 4 -> 5

Time Complexity: O(n)
- Every node is visited at most once.

Space Complexity: O(1)
- Only a few pointers are used.
"""

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Dummy node helps handle cases where the head itself needs to be removed
        dummy = ListNode(-1)
        dummy.next = head

        # prev always points to the last node we are keeping
        curr = dummy
        prev = dummy
        curr = curr.next

        # Traverse the linked list
        while curr:
            # If current node contains the target value
            if curr.val == val:
                # Skip all consecutive nodes having the target value
                while curr and curr.val == val:
                    curr = curr.next

                # Connect the previous valid node to the next valid node
                prev.next = curr
            else:
                # Move both pointers forward when current node is kept
                curr = curr.next
                prev = prev.next

        return dummy.next
