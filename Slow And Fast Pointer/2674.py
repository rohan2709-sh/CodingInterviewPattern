# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:

        # Slow pointer moves 1 step at a time
        slow = list

        # Fast pointer moves 2 steps at a time
        fast = list


        # We stop when fast reaches the end of circular list
        #
        # Case 1:
        # fast.next == list
        # means fast is currently at the last node
        #
        # Case 2:
        # fast.next.next == list
        # means fast is currently at second last node
        #
        # At this point, slow will be at middle node
        while fast.next != list and fast.next.next != list:
            slow = slow.next
            fast = fast.next.next


        # This condition happens when number of nodes is even
        #
        # Example:
        # 2 -> 6 -> 1 -> 5
        #
        # fast stops at node 1
        #
        # We move fast one more step so that
        # fast reaches the actual last node
        if fast.next.next == list:
            fast = fast.next


        # First half starts from original head
        firstHead = list

        # Second half starts from node after slow
        secondHead = slow.next


        # Make first half circular
        #
        # Example:
        # 2 -> 6
        #      |
        #      v
        #      2
        #
        # slow is currently at last node of first half
        slow.next = firstHead


        # Make second half circular
        #
        # Example:
        # 1 -> 5
        #      |
        #      v
        #      1
        #
        # fast is currently at last node of second half
        fast.next = secondHead


        # Return both circular linked lists
        return [firstHead, secondHead]
