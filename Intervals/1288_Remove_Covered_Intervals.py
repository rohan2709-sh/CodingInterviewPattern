# Step-by-step explanation:
#
# First, sort intervals by:
#
# 1. Start value in ascending order.
# 2. If two intervals have the same start value, end value in descending order.
#
# Example:
#
# intervals = [[1,4], [1,3], [2,5]]
#
# After sorting:
#
# [[1,4], [1,3], [2,5]]
#
# Sorting end values in descending order is important because when two intervals
# have the same start, the larger interval should come first.
#
# For example:
#
# [1,3] is covered by [1,4]
#
# So [1,4] must appear before [1,3].
#
# --------------------------------------------------
#
# temp stores intervals that are not covered so far.
#
# index points to the last interval stored in temp.
#
# Initially:
#
# temp = [[1,4]]
# index = 0
#
# --------------------------------------------------
#
# For every next interval:
#
# Check whether its end value is less than or equal to the end value
# of the last interval in temp.
#
# If yes:
#
# The current interval is covered by the last interval in temp.
#
# Example:
#
# temp[index] = [1,4]
# current interval = [2,3]
#
# Since:
#
# 1 <= 2
# 3 <= 4
#
# [2,3] is covered by [1,4].
#
# So we do not add it as a new interval.
#
# --------------------------------------------------
#
# If the current interval is not covered:
#
# Add it to temp.
#
# Example:
#
# temp[index] = [1,4]
# current interval = [3,6]
#
# [3,6] is not covered because:
#
# 6 > 4
#
# So add [3,6] to temp.
#
# --------------------------------------------------
#
# Example:
#
# intervals = [[1,4], [3,6], [2,8]]
#
# After sorting:
#
# [[1,4], [2,8], [3,6]]
#
# Start:
#
# temp = [[1,4]]
#
# --------------------------------------------------
#
# Check [2,8]:
#
# [2,8] is not covered by [1,4] because:
#
# 8 > 4
#
# Add it:
#
# temp = [[1,4], [2,8]]
#
# --------------------------------------------------
#
# Check [3,6]:
#
# [3,6] is covered by [2,8] because:
#
# 2 <= 3
# 6 <= 8
#
# Do not add it.
#
# Final:
#
# temp = [[1,4], [2,8]]
#
# Return:
#
# len(temp) = 2
#
# Time Complexity:
#
# Sorting takes O(n log n).
#
# Loop takes O(n).
#
# Total: O(n log n)
#
# Space Complexity:
#
# temp can store up to n intervals.
#
# Total: O(n)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        temp = []
        index = 0
        temp.append(intervals[0])
        for i in range(1, len(intervals)):
            if temp[index][0] <= intervals[i][1] and temp[index][1] >= intervals[i][1]:
                newStart = min(temp[index][0], intervals[i][0])
                newEnd = max(temp[index][1], intervals[i][1])
                temp[index] = [newStart, newEnd]
            else:
                temp.append(intervals[i])
                index += 1
        return len(temp)
