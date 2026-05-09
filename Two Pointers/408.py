# Algorithm:
#
# 1. Use two pointers:
#    - i       -> to traverse abbreviation string (abbr)
#    - wordIndex -> to traverse original word
#
# 2. Traverse the abbreviation string character by character.
#
# 3. If current character in abbr is a letter:
#      - It must exactly match the current character in word.
#      - If it does not match, return False.
#      - Move both pointers forward.
#
# 4. If current character in abbr is a digit:
#      - Check for leading zero.
#        Example:
#           "01" is invalid
#           "0" is invalid
#
#      - Build the complete number.
#        Example:
#           "12" should be treated as twelve, not '1' and '2'.
#
#      - Skip that many characters in word
#        by increasing wordIndex.
#
# 5. After processing the entire abbreviation:
#      - wordIndex should exactly reach the end of word.
#      - If not, abbreviation is invalid.
#
#
# Example:
#
# word = "internationalization"
# abbr = "i12iz4n"
#
# Steps:
#   i  -> matches 'i'
#   12 -> skip 12 characters
#   i  -> matches 'i'
#   z  -> matches 'z'
#   4  -> skip 4 characters
#   n  -> matches 'n'
#
# Successfully reached end of both strings -> return True
#
#
# Time Complexity:
# O(N)
# where N = length of abbreviation string.
#
# We traverse the abbreviation once.
#
#
# Space Complexity:
# O(1)
#
# No extra data structures are used.
# Only a few variables/pointers are used.
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wordLength = len(word)

        wordIndex = 0
        i = 0

        while i < len(abbr):

            if abbr[i].isalpha():

                # Character must match the corresponding character in word
                if wordIndex >= wordLength or word[wordIndex] != abbr[i]:
                    return False

                wordIndex += 1
                i += 1

            else:

                # Leading zero check
                if abbr[i] == '0':
                    return False

                number = abbr[i]
                j = i + 1

                while j < len(abbr) and abbr[j].isdigit():
                    number = number + abbr[j]
                    j += 1

                # Skip characters in word
                wordIndex += int(number)

                i = j

        return wordIndex == wordLength