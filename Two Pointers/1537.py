# Idea:
# We traverse both sorted arrays using two pointers.
# Since switching is only allowed at common elements,
# we keep track of the score collected from each array separately.
#
# sum1 -> score collected while moving through nums1
# sum2 -> score collected while moving through nums2
#
# While traversing:
#
# 1. If nums1[i] < nums2[j]
#    -> add nums1[i] to sum1 and move i forward.
#
# 2. If nums1[i] > nums2[j]
#    -> add nums2[j] to sum2 and move j forward.
#
# 3. If nums1[i] == nums2[j] (common element)
#    -> we can switch arrays here.
#    -> choose the path with the larger score so far.
#    -> add the common element to that larger score.
#    -> assign this new value to both sums so both paths
#       continue with the best possible score.
#
# This greedy choice works because arrays are strictly increasing,
# so keeping the larger accumulated score always leads to the
# maximum final result.
#
# After processing all elements, return the larger of sum1 and sum2.
#
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        len1 = len(nums1)
        len2 = len(nums2)
        sumPath1 = 0
        sumPath2 = 0
        p1 = 0
        p2 = 0
        while p1 < len1 and p2 < len2:
            if nums1[p1] < nums2[p2]:
                sumPath1 = sumPath1 + nums1[p1]
                p1 += 1
            elif nums2[p2] < nums1[p1]:
                sumPath2 = sumPath2 + nums2[p2]
                p2 += 1
            else:
                sumPath1 = sumPath2 = max(sumPath1, sumPath2) + nums1[p1]
                p1 += 1
                p2 += 1
        while p2 < len2:
            sumPath2 += nums2[p2]
            p2 += 1
        while p1 < len1:
            sumPath1 += nums1[p1]
            p1 += 1
        return max(sumPath1, sumPath2) % MOD
