# --------------------------------------------------
# Step-by-step explanation:
#
# intervals = [[0,30], [5,10], [15,20]]
#
# After sorting:
# intervals = [[0,30], [5,10], [15,20]]
#
# --------------------------------------------------
# Add first meeting [0,30]
#
# min_heap = [30]
#
# One room is currently being used.
#
# --------------------------------------------------
# Check meeting [5,10]
#
# start = 5
# end = 10
# earliest ending meeting = min_heap[0] = 30
#
# Check:
# 5 >= 30  -> False
#
# The meeting [0,30] is still happening when [5,10] starts.
# We cannot reuse the same room.
#
# Push current meeting's end time:
# min_heap = [10, 30]
#
# Now 2 rooms are needed.
#
# --------------------------------------------------
# Check meeting [15,20]
#
# start = 15
# end = 20
# earliest ending meeting = min_heap[0] = 10
#
# Check:
# 15 >= 10  -> True
#
# Meeting [5,10] ends before [15,20] starts.
# So we can reuse that conference room.
#
# Pop 10:
# min_heap = [30]
#
# Push current meeting's end time 20:
# min_heap = [20, 30]
#
# Two rooms are still being used:
# - One room for [0,30]
# - One room for [15,20]
#
# --------------------------------------------------
# Final:
#
# len(min_heap) = 2
#
# Answer = 2
# --------------------------------------------------
import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort meetings by their start time
        intervals.sort()

        # Min heap stores end times of meetings currently using rooms
        min_heap = []

        # Put the first meeting's end time into the heap
        heapq.heappush(min_heap, intervals[0][1])

        # Go through the remaining meetings
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            # If the meeting that ends earliest is finished before
            # the current meeting starts, reuse that conference room.
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Add the current meeting's end time.
            # If we popped, we reused a room.
            # If we did not pop, this means we need a new room.
            heapq.heappush(min_heap, end)

        # Number of end times in heap = number of rooms needed
        return len(min_heap)


