# Step-by-step explanation:
#
# This approach uses:
#
# 1. A min heap:
#    - keeps numbers in sorted order when popped
#
# 2. A set:
#    - prevents duplicate values from being added
#
# Example:
#
# addNum(1)
# addNum(3)
# addNum(7)
# addNum(2)
# addNum(6)
#
# min_heap contains:
#
# [1, 2, 3, 6, 7]
#
# --------------------------------------------------
#
# __init__()
#
# self.min_heap = []
#
# This heap stores all unique numbers that have been added.
#
# A min heap ensures that the smallest number is always removed first.
#
# Example:
#
# min_heap = [1, 3, 7]
#
# heapq.heappop(min_heap) returns:
#
# 1
#
# --------------------------------------------------
#
# self.seen = set()
#
# This set keeps track of values already added.
#
# Example:
#
# self.seen = {1, 3, 7}
#
# If addNum(3) is called again,
# we do not push 3 into the heap again.
#
# --------------------------------------------------
#
# addNum(value)
#
# if value not in self.seen:
#
# Check whether value has already been added.
#
# Example:
#
# self.seen = {1, 3, 7}
# value = 3
#
# 3 is already in self.seen.
#
# So we do nothing.
#
# This prevents duplicate intervals or duplicate heap values.
#
# --------------------------------------------------
#
# heapq.heappush(self.min_heap, value)
#
# Add value to the min heap.
#
# Example:
#
# min_heap = [1, 3, 7]
# value = 2
#
# After pushing 2:
#
# min_heap contains:
#
# [1, 2, 7, 3]
#
# Important:
#
# A heap is not fully sorted internally.
#
# But every time we pop from it,
# heapq.heappop() always returns the smallest value.
#
# Popping all values gives:
#
# 1, 2, 3, 7
#
# --------------------------------------------------
#
# self.seen.add(value)
#
# Add value to the set so duplicates can be ignored later.
#
# --------------------------------------------------
#
# getIntervals()
#
# Goal:
#
# Pop numbers in sorted order and combine consecutive numbers
# into intervals.
#
# Example:
#
# Numbers:
#
# 1, 2, 3, 6, 7
#
# Intervals:
#
# [[1, 3], [6, 7]]
#
# --------------------------------------------------
#
# if not self.min_heap:
#     return []
#
# If no numbers have been added yet,
# there are no intervals to return.
#
# --------------------------------------------------
#
# min_heap_copy = self.min_heap[:]
#
# Create a copy of the heap.
#
# We use a copy because getIntervals() should not remove
# numbers from the original heap.
#
# Example:
#
# self.min_heap = [1, 2, 3, 6, 7]
#
# min_heap_copy = [1, 2, 3, 6, 7]
#
# We pop from min_heap_copy only.
#
# self.min_heap remains unchanged.
#
# --------------------------------------------------
#
# output = []
#
# This stores the final list of intervals.
#
# Example:
#
# output = [[1, 3], [6, 7]]
#
# --------------------------------------------------
#
# start = heapq.heappop(min_heap_copy)
#
# Remove the smallest number from the heap.
#
# This becomes the start of the first interval.
#
# Example:
#
# min_heap_copy contains values:
#
# 1, 2, 3, 6, 7
#
# start = 1
#
# --------------------------------------------------
#
# end = start
#
# Initially, the interval contains only one number.
#
# start = 1
# end = 1
#
# Current interval:
#
# [1, 1]
#
# --------------------------------------------------
#
# while min_heap_copy:
#
# Continue until every number in the copied heap is processed.
#
# --------------------------------------------------
#
# current = heapq.heappop(min_heap_copy)
#
# Get the next smallest number.
#
# Example:
#
# current values will be processed in this order:
#
# 2, 3, 6, 7
#
# --------------------------------------------------
#
# if current == end + 1:
#
# Check whether current is consecutive with the current interval.
#
# Example:
#
# Current interval:
#
# [1, 1]
#
# current = 2
#
# 2 == 1 + 1
#
# True
#
# So 2 continues the current interval.
#
# --------------------------------------------------
#
# end = current
#
# Extend the current interval.
#
# Example:
#
# start = 1
# end = 1
# current = 2
#
# After updating:
#
# start = 1
# end = 2
#
# Current interval:
#
# [1, 2]
#
# --------------------------------------------------
#
# Next:
#
# current = 3
#
# 3 == end + 1
# 3 == 2 + 1
#
# True
#
# Extend interval:
#
# [1, 2] -> [1, 3]
#
# --------------------------------------------------
#
# else:
#
# This means current is not consecutive with end.
#
# Example:
#
# Current interval:
#
# [1, 3]
#
# current = 6
#
# 6 != 3 + 1
#
# So 6 cannot be part of [1, 3].
#
# The interval [1, 3] is complete.
#
# --------------------------------------------------
#
# output.append([start, end])
#
# Save the completed interval.
#
# Example:
#
# output = [[1, 3]]
#
# --------------------------------------------------
#
# start = current
# end = current
#
# Start a new interval using current.
#
# Example:
#
# current = 6
#
# start = 6
# end = 6
#
# Current interval:
#
# [6, 6]
#
# --------------------------------------------------
#
# Next:
#
# current = 7
#
# 7 == end + 1
# 7 == 6 + 1
#
# True
#
# Extend current interval:
#
# [6, 6] -> [6, 7]
#
# --------------------------------------------------
#
# output.append([start, end])
#
# After the loop finishes,
# the final interval has not yet been added to output.
#
# So add it.
#
# Example:
#
# output = [[1, 3]]
#
# Final interval:
#
# [6, 7]
#
# Final output:
#
# [[1, 3], [6, 7]]
#
# --------------------------------------------------
#
# Time Complexity:
#
# addNum(value):
#
# O(log n)
#
# because adding an item to a heap takes O(log n).
#
# --------------------------------------------------
#
# getIntervals():
#
# O(n log n)
#
# because we pop all n values from the copied heap,
# and each heap pop takes O(log n).
#
# --------------------------------------------------
#
# Space Complexity:
#
# O(n)
#
# because we store:
#
# - n values in min_heap
# - n values in seen
# - a copied heap during getIntervals()
# - output intervals

import heapq
from typing import List

class SummaryRanges:

    def __init__(self):
        self.min_heap = []
        self.seen = set()

    def addNum(self, value: int) -> None:
        # Avoid duplicates
        if value not in self.seen:
            heapq.heappush(self.min_heap, value)
            self.seen.add(value)

    def getIntervals(self) -> List[List[int]]:
        if not self.min_heap:
            return []

        min_heap_copy = self.min_heap[:]
        output = []

        start = heapq.heappop(min_heap_copy)
        end = start

        while min_heap_copy:
            current = heapq.heappop(min_heap_copy)

            # Consecutive number: extend current interval
            if current == end + 1:
                end = current
            else:
                # Current interval is complete
                output.append([start, end])

                # Start a new interval
                start = current
                end = current

        # Add final interval
        output.append([start, end])

        return output
