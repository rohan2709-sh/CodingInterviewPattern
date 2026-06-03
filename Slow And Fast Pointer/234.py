# ---------------------------------------------------
# Intuition:
# ---------------------------------------------------
# A palindrome reads the same forward and backward.
#
# Since this is a singly linked list,
# we cannot move backward directly.
#
# Approach:
#
# 1. Find the middle of the linked list
#    using slow and fast pointers.
#
# 2. If the length is odd,
#    skip the middle node because
#    it does not affect palindrome checking.
#
# 3. Reverse the second half of the list.
#
# 4. Compare the first half and
#    reversed second half node by node.
#
# 5. If all values match -> palindrome.
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

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
        # Step 2: Handle odd length list
        # ---------------------------------------------------
        # If fast is not None,
        # list length is odd.
        #
        # Example:
        # 1 -> 2 -> 3 -> 2 -> 1
        #
        # slow is at 3
        # We skip middle element
        if fast:
            slow = slow.next

        # ---------------------------------------------------
        # Step 3: Reverse second half
        # ---------------------------------------------------
        prev = None
        curr = slow

        while curr:

            # Store next node
            next_node = curr.next

            # Reverse pointer
            curr.next = prev

            # Move prev forward
            prev = curr

            # Move curr forward
            curr = next_node

        # ---------------------------------------------------
        # Step 4: Compare both halves
        # ---------------------------------------------------
        # head -> first half
        # prev -> reversed second half
        curr = head

        while prev != None:

            # If values differ,
            # not a palindrome
            if curr.val != prev.val:
                return False

            curr = curr.next
            prev = prev.next

        # All nodes matched
        return True
