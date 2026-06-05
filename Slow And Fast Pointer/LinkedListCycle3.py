# Question:
#
# Given the head of a linked list, determine the length of
# the cycle present in the linked list.
#
# If there is no cycle, return 0.
#
# A cycle exists in a linked list if some node can be reached
# again by continuously following the next pointer.
#
#
# Example:
#
# 1 -> 2 -> 3 -> 4 -> 5
#           ^         |
#           |_________|
#
# Here the cycle is:
# 3 -> 4 -> 5 -> 3
#
# Cycle length = 3
#
#
# Approach Used:
#
# We use Floyd’s Cycle Detection Algorithm
# (also called Slow and Fast Pointer approach).
#
#
# Step 1:
# Detect whether a cycle exists.
#
# slow moves 1 step at a time
# fast moves 2 steps at a time
#
# If slow and fast meet,
# then a cycle exists.
#
#
# Step 2:
# If no cycle exists,
# return 0.
#
#
# Step 3:
# Move slow back to head.
#
# Now move:
# slow = slow.next
# fast = fast.next
#
# one step at a time.
#
# The point where they meet again
# is the starting node of the cycle.
#
#
# Step 4:
# Store the cycle starting node.
#
# Traverse the cycle once completely
# until we reach the same node again.
#
# Count the number of nodes visited.
#
# That count is the cycle length.
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

def count_cycle_length(head):

   slow = head
   fast = head
   cycleDetected = False
   
   # Detect cycle using slow and fast pointers
   while fast != None and fast.next != None:
      slow = slow.next
      fast = fast.next.next

      # If both pointers meet,
      # cycle exists
      if slow == fast:
         cycleDetected = True
         break
   
   # No cycle found
   if not cycleDetected:
      return 0
   
   # Move slow back to head
   slow = head

   # Move both pointers one step at a time
   # They will meet at cycle starting node
   while slow != fast:
      slow = slow.next
      fast = fast.next
   
   # Store cycle starting node
   cycleNode = slow

   # Start counting cycle length
   cycleLength = 1

   # Move slow ahead by one step
   slow = slow.next
   
   # Traverse entire cycle
   while slow != cycleNode:
      cycleLength += 1
      slow = slow.next
   
   return cycleLength
