# We first sort the intervals by their start time.
# This ensures that any overlapping intervals will appear next to each other.
#
# Example:
# intervals = [[1,3],[2,6],[8,10],[15,18]]
#
# After sorting:
# [[1,3],[2,6],[8,10],[15,18]]
#
# ------------------------------------------------------------------
# We initialize the output list with the first interval because
# there is nothing before it to compare against.
#
# output = [[1,3]]
#
# ------------------------------------------------------------------
# For each remaining interval:
#
# Check if it overlaps with the last interval stored in output.
#
# Overlap condition:
# output[index][1] >= intervals[i][0]
#
# Meaning:
# previous_end >= current_start
#
# If true:
#   Merge the intervals by:
#   - taking the smaller start value
#   - taking the larger end value
#
# If false:
#   No overlap exists, so add the current interval
#   as a new interval in output.
#
# ------------------------------------------------------------------
# Walkthrough Example:
#
# intervals = [[1,3],[2,6],[8,10],[15,18]]
#
# Initial:
# output = [[1,3]]
#
# i = 1 -> [2,6]
#
# Compare:
# output[-1] = [1,3]
# 3 >= 2  -> overlap
#
# Merge:
# start = min(1,2) = 1
# end   = max(3,6) = 6
#
# output = [[1,6]]
#
# ---------------------------------------------------
# i = 2 -> [8,10]
#
# Compare:
# output[-1] = [1,6]
# 6 >= 8 -> False
#
# No overlap.
#
# output = [[1,6],[8,10]]
#
# ---------------------------------------------------
# i = 3 -> [15,18]
#
# Compare:
# output[-1] = [8,10]
# 10 >= 15 -> False
#
# No overlap.
#
# output = [[1,6],[8,10],[15,18]]
#
# ---------------------------------------------------
# Final Answer:
# [[1,6],[8,10],[15,18]]
#
# ------------------------------------------------------------------
# Example 2:
#
# intervals = [[1,4],[4,5]]
#
# output = [[1,4]]
#
# Compare [4,5]:
# 4 >= 4 -> overlap
#
# Merge:
# start = min(1,4) = 1
# end   = max(4,5) = 5
#
# output = [[1,5]]
#
# Final Answer:
# [[1,5]]
#
# ------------------------------------------------------------------
# Time Complexity:
# Sorting: O(n log n)
# Traversing intervals: O(n)
#
# Overall: O(n log n)
#
# Space Complexity:
# O(n) for the output list.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        output.append(intervals[0])
        index = 0
        for i in range(1, len(intervals)):
            temp = []
            if output[index][1] >= intervals[i][0]:
                temp.append(min(intervals[i][0], output[index][0]))
                temp.append(max(intervals[i][1], output[index][1]))
                output[index] = temp
            else:
                temp.append(intervals[i][0])
                temp.append(intervals[i][1])
                output.append(temp)
                index += 1
        return output
