# Since intervals are already sorted and non-overlapping:
#
# 1. Add all intervals that end before newInterval starts.
#
# Example:
# intervals   = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]
#
# [1,2] ends before 4 -> add to result
#
# result = [[1,2]]
#
# 2. Merge all overlapping intervals.
#
# [3,5] overlaps with [4,8]
# merged -> [3,8]
#
# [6,7] overlaps with [3,8]
# merged -> [3,8]
#
# [8,10] overlaps with [3,8]
# merged -> [3,10]
#
# result = [[1,2],[3,10]]
#
# 3. Add remaining intervals.
#
# Add [12,16]
#
# Final result:
# [[1,2],[3,10],[12,16]]
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1) Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2) Merge all intervals that overlap with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # 3) Add the rest
        while i < n:
            res.append(intervals[i])
            i += 1

        return res
