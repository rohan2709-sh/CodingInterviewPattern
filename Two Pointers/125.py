"""
        Explanation

        We use the Two Pointer approach.

        Goal:
        Check whether the string is a palindrome after:
        1. Converting uppercase letters to lowercase
        2. Ignoring non-alphanumeric characters

        Two pointers are used:
        left  -> starts from beginning of string
        right -> starts from end of string

        We compare characters from both ends.

        Important:
        - If a character is NOT alphanumeric,
          we skip it using isalnum().
        - Comparison is done using lower()
          so uppercase and lowercase are treated equally.

        Example:
        s = "A man, a plan, a canal: Panama"

        Step-by-step:

        left = 'A'
        right = 'a'

        Convert both to lowercase:
        'a' == 'a' -> valid

        Move both pointers inward.

        Skip spaces, commas, and colons because:
        character.isalnum() == False

        Continue comparing characters:
        a == a
        m == m
        a == a
        n == n
        ...

        Since all valid characters match,
        the string is a palindrome.

        If at any point characters do not match:
        return False

        If loop completes successfully:
        return True

        Time Complexity:
        O(n)
        -> each character is visited at most once

        Space Complexity:
        O(1)
        -> no extra space used
        """
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        left = 0
        right = len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True