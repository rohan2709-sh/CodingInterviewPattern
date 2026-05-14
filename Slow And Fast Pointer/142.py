# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # We use Floyd's Cycle Detection Algorithm
        # (also called Slow and Fast Pointer approach).
        #
        # Goal:
        # - Detect whether a cycle exists
        # - Find the exact node where the cycle starts
        #
        # Idea:
        # - slowPointer moves 1 step at a time
        # - fastPointer moves 2 steps at a time
        #
        # If there is a cycle:
        # slowPointer and fastPointer will eventually meet.
        #
        # After meeting:
        # - Move slowPointer back to head
        # - Move both pointers one step at a time
        # - The node where they meet again
        #   is the starting node of the cycle

        slowPointer = head
        fastPointer = head

        cycleDetected = False

        # Traverse the linked list
        while fastPointer != None and fastPointer.next != None:

            # Move slow pointer by 1 step
            slowPointer = slowPointer.next

            # Move fast pointer by 2 steps
            fastPointer = fastPointer.next.next

            # If both pointers meet,
            # cycle exists
            if slowPointer == fastPointer:
                cycleDetected = True
                break

        # If cycle was never detected,
        # return None
        if not cycleDetected:
            return None

        # Move slow pointer back to head
        slowPointer = head

        # Move both pointers one step at a time
        #
        # The node where they meet
        # will be the starting node of cycle
        while slowPointer != fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next

        # Return the starting node of cycle
        return slowPointer