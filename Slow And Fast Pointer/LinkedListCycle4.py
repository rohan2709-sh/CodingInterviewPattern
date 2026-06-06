# Question:
#
# Given the head of a singly linked list,
# detect and remove the cycle present in the list.
#
# A cycle occurs when a node points back
# to a previously visited node.
#
# The linked list must be modified in-place
# and should remain in the same order after
# removing the cycle.
#
# If no cycle exists, return the list as it is.
#
#
# Example:
#
# 1 -> 2 -> 3 -> 4 -> 5
#           ^         |
#           |_________|
#
# Cycle starts at node 3.
#
# After removing cycle:
#
# 1 -> 2 -> 3 -> 4 -> 5 -> None
#
#
# Approach Used:
#
# We use Floyd’s Cycle Detection Algorithm
# (Slow and Fast Pointer approach).
#
#
# Step 1:
# Detect whether a cycle exists.
#
# slow moves one step at a time
# fast moves two steps at a time
#
# If slow == fast,
# then cycle exists.
#
#
# Step 2:
# If no cycle exists,
# return head.
#
#
# Step 3:
# Move slow back to head.
#
# Move both slow and fast
# one step at a time.
#
# The node where they meet again
# is the starting node of the cycle.
#
#
# Step 4:
# Store the cycle start node.
#
# Traverse the cycle until reaching
# the node whose next points to
# the cycle start node.
#
#
# Step 5:
# Remove cycle by setting:
#
# lastNode.next = None
#
#
# Time Complexity:
# O(n)
#
# Space Complexity:
# O(1)

# The first input of the test case is an array of values representing a linked list. 
# The second input is the index where the tail connects to form a cycle (or −1 if there's no cycle). 
# This index is used only to construct the linked list and is not passed to the function.

# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from ds_v1.LinkedList.LinkedList import ListNode

def remove_cycle(head):
    slow = head
    fast = head
    cycleDetected = False
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycleDetected = True
            break
    if not cycleDetected:
        return head
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    curr = slow
    slow = slow.next
    while slow.next != curr:
        slow = slow.next
    slow.next = None
            
    return head
