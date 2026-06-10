# We use a Fixed-Size Sliding Window because we need the sum of every
# contiguous subarray of length k.
#
# 1. First, compute the sum of the initial window containing the first
#    k elements.
#
# 2. Evaluate this window:
#       - If the sum is less than lower, lose 1 point.
#       - If the sum is greater than upper, gain 1 point.
#       - Otherwise, no change.
#
# 3. Slide the window one position at a time:
#       - Add the new element entering the window.
#       - Remove the old element leaving the window.
#
#    New Window Sum =
#       Previous Window Sum
#       + incoming element
#       - outgoing element
#
# 4. After updating the window sum, evaluate the new window and
#    update the score accordingly.
#
# 5. Continue until all windows of size k have been processed.
#
# Example:
# calories = [1,2,3,4,5], k = 3
#
# Window [1,2,3] -> sum = 6
# Slide:
#     remove 1, add 4
# Window [2,3,4] -> sum = 9
# Slide:
#     remove 2, add 5
# Window [3,4,5] -> sum = 12
#
# Time Complexity: O(n)
# - Initial sum takes O(k).
# - Each remaining window is processed in O(1).
# - Total complexity is O(n).
#
# Space Complexity: O(1)
# - Only a few variables are used.
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        windowSum = sum(calories[:k])
        points = 0

        if windowSum < lower:
            points -= 1
        elif windowSum > upper:
            points += 1

        for i in range(k, len(calories)):
            windowSum += calories[i]
            windowSum -= calories[i - k]

            if windowSum < lower:
                points -= 1
            elif windowSum > upper:
                points += 1

        return points
