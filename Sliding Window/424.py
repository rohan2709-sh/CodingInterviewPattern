class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # count -> stores frequency of characters inside current window
        count = {}

        # res -> stores length of longest valid substring
        res = 0

        # left pointer of sliding window
        l = 0

        # Expand window using right pointer
        for r in range(len(s)):

            # Add current character into frequency map
            count[s[r]] = 1 + count.get(s[r], 0)

            # ---------------------------------------------------------
            # Key Idea:
            #
            # Window size = (r - l + 1)
            #
            # max(count.values()) gives frequency of most common character
            # inside current window.
            #
            # Characters to replace =
            # window size - most frequent character count
            #
            # Example:
            # Window = "AABAB"
            #
            # Counts:
            # A -> 3
            # B -> 2
            #
            # Window size = 5
            # Most frequent count = 3
            #
            # Replacements needed = 5 - 3 = 2
            #
            # Meaning:
            # Replace 2 B's with A's to make all characters same.
            #
            # If replacements needed become greater than k,
            # window becomes invalid.
            # ---------------------------------------------------------

            while (r - l + 1) - max(count.values()) > k:

                # Remove left character from window
                count[s[l]] -= 1

                # Shrink window from left
                l += 1

            # Current window is valid
            # Update maximum length found so far
            res = max(res, r - l + 1)

        return res
