# We use the Sliding Window technique because all numbers are positive.
#
# 1. Expand the window by moving 'end' and adding nums[end] to currentSum.
#
# 2. As soon as currentSum becomes greater than or equal to target,
#    the current window is a valid answer.
#
# 3. Record its length and then try to shrink the window from the left
#    to see if we can find an even smaller valid window.
#
# 4. Continue shrinking while the window sum is still >= target.
#
# 5. Since all numbers are positive, removing elements from the left
#    can only decrease the sum, making Sliding Window work efficiently.
#
# Example:
# target = 11
# nums = [1,2,3,4,5]
#
# Window [1,2,3,4,5] -> sum = 15
# Length = 5
#
# Shrink:
# Window [2,3,4,5] -> sum = 14
# Length = 4
#
# Shrink:
# Window [3,4,5] -> sum = 12
# Length = 3
#
# Shrink:
# Window [4,5] -> sum = 9 (< 11)
#
# Smallest valid length found = 3
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        start = 0
        currentSum = 0
        minLength = float('inf')

        for end in range(len(nums)):
            currentSum += nums[end]

            # While current window satisfies the condition,
            # try shrinking it from the left to find a smaller valid window.
            while currentSum >= target:
                minLength = min(minLength, end - start + 1)

                currentSum -= nums[start]
                start += 1

        return minLength if minLength != float('inf') else 0
