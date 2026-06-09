# Explanation

# We use the Sliding Window technique.

# start -> left side of the window
# end   -> right side of the window

# A set is used to keep track of characters
# currently inside the window.

# If the current character is not present in the set:
#   - add it to the set
#   - expand the window by moving end

# If the current character already exists:
#   - we found a duplicate
#   - calculate current valid window length
#   - shrink the window from the left side
#     until the duplicate is removed

# The window always contains unique characters.

# At the end, return the maximum substring length found.


# Example:
# s = "abcabcbb"

# Window progression:
# "a"
# "ab"
# "abc"

# Duplicate 'a' found:
# Remove characters from left until duplicate is removed

# New windows:
# "bca"
# "cab"

# Maximum length = 3


# Time Complexity: O(n)
# Each character is added and removed at most once.

# Space Complexity: O(k)
# k = number of unique characters in current window.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        mySet = set()

        start = 0
        end = 1

        mySet.add(s[start])

        difference = 0

        while end < len(s):

            # Duplicate found, shrink window
            if s[end] in mySet:

                difference = max(difference, end - start)

                while s[end] in mySet:
                    mySet.remove(s[start])
                    start += 1

            # Add current character into window
            mySet.add(s[end])

            # Expand window
            end += 1

        return max(difference, end - start)
