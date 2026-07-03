"""
------------------------------------ INTUITION ------------------------------------

The required order is:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 ...

Notice that nodes are taken alternately from:
1. The beginning of the list.
2. The end of the list.

Since a singly linked list cannot be traversed backwards efficiently,
we first reverse the second half of the list. After reversing, the last
node becomes the first node of the second half, allowing us to merge both
halves in the required alternating order.

The solution consists of three simple steps:
1. Find the middle of the linked list.
2. Reverse the second half.
3. Merge the first half and reversed second half alternately.


------------------------------------ EXPLANATION ------------------------------------

Example:

Original List:
1 → 2 → 3 → 4 → 5

Step 1: Find the middle

slow stops at 3.

First Half:
1 → 2 → 3

Second Half:
4 → 5


Step 2: Reverse the second half

4 → 5

becomes

5 → 4


Step 3: Merge alternately

First Half:
1 → 2 → 3

Second Half:
5 → 4

Iteration 1:
1 → 5 → 2 → 3
        ^
        Remaining second half: 4

Iteration 2:
1 → 5 → 2 → 4 → 3

Final Answer:
1 → 5 → 2 → 4 → 3


Why initialize fast = head.next?

This ensures that for even-length lists, the slow pointer stops at the
last node of the first half.

Example:

1 → 2 → 3 → 4

slow ends at 2

First Half:
1 → 2

Second Half:
3 → 4

which splits the list evenly.


Time Complexity:
- Finding middle: O(n)
- Reversing second half: O(n)
- Merging: O(n)

Overall: O(n)

Space Complexity:
O(1)

Only a few pointers are used; no extra data structures are required.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Get the middle node using slow and fast pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None

        # Reverse the second half
        reverseList = self.reverse(second)

        # Merge the two halves alternately
        firstHalf = head
        while reverseList:
            temp1 = firstHalf.next
            temp2 = reverseList.next

            firstHalf.next = reverseList
            reverseList.next = temp1

            firstHalf = temp1
            reverseList = temp2

    def reverse(self, second):
        curr = second
        prev = None

        # Standard iterative linked list reversal
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
