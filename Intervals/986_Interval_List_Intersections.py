# Explanation:
#
# We use two pointers:
# - i for firstList
# - j for secondList
#
# Since both lists are already sorted and each list contains non-overlapping
# intervals, we can compare one interval from each list at a time.
#
# For the current intervals:
# firstList[i]  = [start1, end1]
# secondList[j] = [start2, end2]
#
# Their intersection starts at the later start time:
# latestStartTime = max(start1, start2)
#
# Their intersection ends at the earlier end time:
# latestEndTime = min(end1, end2)
#
# If latestStartTime <= latestEndTime, the intervals overlap.
# So, we add [latestStartTime, latestEndTime] to output.
#
# Example:
# firstList[i]  = [1, 5]
# secondList[j] = [3, 7]
#
# latestStartTime = max(1, 3) = 3
# latestEndTime = min(5, 7) = 5
#
# Since 3 <= 5, the intersection is [3, 5].
#
# After checking the intersection, move the pointer of the interval
# that ends first.
#
# Why?
# The interval that ends first cannot overlap with any future interval
# from the other list, because all future intervals start after the
# current interval in their sorted list.
#
# If secondList[j] ends before firstList[i], move j forward.
# Otherwise, move i forward.
#
# Time Complexity: O(m + n)
# Each interval from both lists is processed at most once.
#
# Space Complexity: O(1)
# Excluding the output list, we only use two pointers and a few variables.
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            latestStartTime = max(firstList[i][0], secondList[j][0])
            latestEndTime = min(firstList[i][1], secondList[j][1])
            if latestStartTime <= latestEndTime:
                res = []
                res.append(latestStartTime)
                res.append(latestEndTime)
                output.append(res)
            if secondList[j][1] < firstList[i][1]:
                j += 1
            else:
                i += 1
        return output
