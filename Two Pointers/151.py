# Algorithm:
#
# Step 1:
# Split the input string into individual words using split().
# split() automatically removes extra spaces.
#
# Example:
# "  the sky   is blue  "
# becomes:
# ["the", "sky", "is", "blue"]
#
# Step 2:
# Initialize two pointers:
# left  -> starting index of list
# right -> ending index of list
#
# Step 3:
# While left pointer is smaller than right pointer:
#   - Swap the words at left and right positions
#   - Move left pointer forward
#   - Move right pointer backward
#
# This reverses the order of words in-place.
#
# Step 4:
# Join all words using a single space.
#
# Step 5:
# Return the final reversed string.
# Time Complexity is O(n) and Space complexity is O(1)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        left = 0
        right = len(words) - 1
        while left < right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -= 1
        return " ".join(words)