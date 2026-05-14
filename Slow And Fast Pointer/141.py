# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # We use Floyd's Cycle Detection Algorithm
        # (also called Slow and Fast Pointer approach).
        #
        # Goal:
        # Determine whether a linked list contains a cycle.
        #
        # Idea:
        # - slowPointer moves 1 step at a time
        # - fastPointer moves 2 steps at a time
        #
        # If there is NO cycle:
        # fastPointer will eventually reach None.
        #
        # If there IS a cycle:
        # fastPointer will eventually catch up
        # with slowPointer inside the cycle.

        slowPointer = head
        fastPointer = head

        # Traverse the linked list
        while fastPointer != None and fastPointer.next != None:

            # Move slow pointer by 1 step
            slowPointer = slowPointer.next

            # Move fast pointer by 2 steps
            fastPointer = fastPointer.next.next

            # If both pointers meet,
            # cycle exists
            if slowPointer == fastPointer:
                return True

        # If fastPointer reaches None,
        # there is no cycle
        return False