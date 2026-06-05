# ---------------------------------------------------
# Intuition:
# ---------------------------------------------------
# We need to find the maximum twin sum.
#
# Twin nodes are:
# ith node and (n - 1 - i)th node
#
# Example:
# 5 -> 4 -> 2 -> 1
#
# Twin pairs:
# 5 + 1 = 6
# 4 + 2 = 6
#
# Since linked lists cannot be traversed backward,
# we use this approach:
#
# 1. Find the middle of the linked list
#    using slow and fast pointers.
#
# 2. Reverse the second half of the list.
#
# 3. Traverse both halves together:
#    - first half from head
#    - second half from reversed list
#
# 4. Compute twin sums and track maximum.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Initialize slow and fast pointers
        slow = head
        fast = head

        # ---------------------------------------------------
        # Step 1: Find middle of linked list
        # ---------------------------------------------------
        # slow moves 1 step
        # fast moves 2 steps
        #
        # When fast reaches end,
        # slow will be at middle
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        # ---------------------------------------------------
        # This condition is not needed for this problem
        # because the linked list length is always even.
        #
        # It is commonly used for odd-length lists
        # to skip the middle element.
        # ---------------------------------------------------
        if fast != None:
            slow = slow.next

        # ---------------------------------------------------
        # Step 2: Reverse second half
        # ---------------------------------------------------
        prev = None
        curr = slow

        while curr:

            # Store next node
            next_node = curr.next

            # Reverse current pointer
            curr.next = prev

            # Move prev forward
            prev = curr

            # Move curr forward
            curr = next_node

        # ---------------------------------------------------
        # Step 3: Calculate twin sums
        # ---------------------------------------------------
        # curr -> first half
        # prev -> reversed second half
        curr = head

        maxSum = 0

        while prev != None:

            # Calculate current twin sum
            tempSum = curr.val + prev.val

            # Update maximum twin sum
            maxSum = max(tempSum, maxSum)

            # Move both pointers
            curr = curr.next
            prev = prev.next

        # Return maximum twin sum
        return maxSum
