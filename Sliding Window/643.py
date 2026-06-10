# We use the Sliding Window technique because we need to examine
# every contiguous subarray of fixed length k.
#
# 1. Maintain the sum of the current window using currSum.
#
# 2. Keep expanding the window by adding nums[i] to currSum.
#
# 3. Once the window size exceeds k:
#    - Calculate the average of the current window.
#    - Update the maximum average found so far.
#    - Remove the leftmost element from the window.
#    - Move the start pointer forward.
#
# 4. After the loop, process the final window since its average
#    has not yet been calculated.
#
# 5. Return the largest average among all windows of size k.
#
# Example:
# nums = [1,12,-5,-6,50,3]
# k = 4
#
# Window [1,12,-5,-6]
# Sum = 2
# Average = 0.5
# Max Average = 0.5
#
# Slide window:
# Remove 1, Add 50
#
# Window [12,-5,-6,50]
# Sum = 51
# Average = 12.75
# Max Average = 12.75
#
# Slide window:
# Remove 12, Add 3
#
# Window [-5,-6,50,3]
# Sum = 42
# Average = 10.5
# Max Average = 12.75
#
# Answer = 12.75
#
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        start = 0
        output = -100000.00
        for i in range(len(nums)):
            if i >= k:
                average = currSum / k
                output = max(average, output)
                currSum -= nums[start]
                start += 1
            currSum += nums[i]
        average = currSum / k
        output = max(average, output)
        return output
