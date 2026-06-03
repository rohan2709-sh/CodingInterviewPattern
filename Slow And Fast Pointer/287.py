# ---------------------------------------------------
# Intuition:
# ---------------------------------------------------
# Treat the array like a linked list.
#
# Example:
# nums = [1,3,4,2,2]
#
# Index -> Value
# 0 -> 1
# 1 -> 3
# 3 -> 2
# 2 -> 4
# 4 -> 2
#
# Since one number is duplicated,
# multiple indices point to the same value,
# which creates a cycle.
#
# We use Floyd’s Cycle Detection Algorithm:
#
# Phase 1:
# Detect if a cycle exists using slow and fast pointers.
#
# Phase 2:
# Find the starting point of the cycle,
# which is the duplicate number.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]

        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps

            if slow == fast:
                break

        # Phase 2: Find duplicate number
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
