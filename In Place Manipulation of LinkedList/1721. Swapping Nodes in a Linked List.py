# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
------------------------------------ INTUITION ------------------------------------

Instead of physically swapping the nodes (which requires changing pointers),
we only swap their values.

To do this, we need to locate:
1. The kth node from the beginning.
2. The kth node from the end.

Since this is a singly linked list, we cannot directly move backwards,
so we first determine the length of the list.

After knowing the length:
- kth node from the beginning is easy to identify.
- kth node from the end is equivalent to the
  (length - k + 1)th node from the beginning.

Using a dummy node slightly shifts the indexing, so after counting the dummy:
- kth node from the beginning is found when size == k.
- kth node from the end is reached after moving (size - k) steps
  from the dummy node.

Finally, swap their values.

------------------------------------ EXAMPLE ------------------------------------

head = [1,2,3,4,5]
k = 2

Pass 1:
(dummy) -> 1 -> 2 -> 3 -> 4 -> 5

size progression:
dummy : 0
1     : 1
2     : 2  <-- firstNode
3     : 3
4     : 4
5     : 5

Final size = 6 (includes dummy)

limit = size - k
      = 6 - 2
      = 4

Move 4 steps from dummy:

Step 0 : dummy
Step 1 : 1
Step 2 : 2
Step 3 : 3
Step 4 : 4 <-- secondNode

Swap values:

2 <-> 4

Result:
[1,4,3,2,5]

------------------------------------ TIME COMPLEXITY ------------------------------------

First traversal : O(n)
Second traversal: O(n)

Overall: O(n)

------------------------------------ SPACE COMPLEXITY ------------------------------------

Only a few pointers are used.

O(1)
"""

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        curr = dummy
        size = 0

        # First pass:
        # Find the length of the list.
        # Since we start from the dummy node, when size == k,
        # curr points to the kth node from the beginning.
        while curr:
            if size == k:
                firstNode = curr
            curr = curr.next
            size += 1

        curr = dummy
        count = 0
        limit = size - k

        # Move to the kth node from the end.
        # size includes the dummy node, so moving (size - k)
        # steps from dummy lands at the kth node from the end.
        while count < limit:
            curr = curr.next
            count += 1

        secondNode = curr

        # Swap only the values of the two nodes.
        temp = firstNode.val
        firstNode.val = secondNode.val
        secondNode.val = temp

        return head


