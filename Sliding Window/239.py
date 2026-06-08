# Problem: Sliding Window Maximum
#
# We are given an array nums and a window size k.
# We need to find the maximum value in every window of size k.

# --------------------------------------------------------
# Key Idea:
#
# We maintain a data structure (deque)
# that always keeps "useful" elements only.
#
# The deque stores INDICES (not values).
#
# --------------------------------------------------------
# Why store indices instead of values?
#
# Because we need to:
# 1. Check if an element is outside the window
# 2. Access the actual value using nums[index]
#
# --------------------------------------------------------
# Important Property of Deque:
#
# We maintain elements in decreasing order of value.
#
# So:
# Front of deque = maximum element of current window
#
# --------------------------------------------------------
# Step-by-step logic:

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        dq = deque()   # stores indices
        output = []

        for i in range(len(nums)):

            # ------------------------------------------------
            # STEP 1: Remove out-of-window elements
            #
            # Current window is [i-k+1, i]
            # If dq[0] < i-k+1, it's outside window → remove
            # ------------------------------------------------
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # ------------------------------------------------
            # STEP 2: Maintain decreasing order in deque
            #
            # If current element is bigger than elements at back,
            # those elements will never be useful again.
            #
            # So remove them.
            # ------------------------------------------------
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # ------------------------------------------------
            # STEP 3: Add current index
            # ------------------------------------------------
            dq.append(i)

            # ------------------------------------------------
            # STEP 4: Start recording results
            #
            # We only start when first full window is formed.
            # That happens when i >= k - 1
            #
            # Front of deque = maximum of current window
            # ------------------------------------------------
            if i >= k - 1:
                output.append(nums[dq[0]])

        return output


# --------------------------------------------------------
# Final Intuition:
#
# - Deque keeps only "possible maximum candidates"
# - Old elements are removed (out of window)
# - Smaller elements are removed (useless forever)
# - Front always gives the maximum in O(1)
#
# Overall time complexity: O(n)
