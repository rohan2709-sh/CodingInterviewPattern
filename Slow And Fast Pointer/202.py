class Solution:
    def isHappy(self, n: int) -> bool:

        # We use Floyd's Cycle Detection Algorithm
        # (also called Slow and Fast Pointer approach).
        #
        # Idea:
        # - A happy number eventually becomes 1.
        # - A non-happy number falls into a repeating cycle.
        #
        # So:
        # - slowPointer moves one step at a time
        # - fastPointer moves two steps at a time
        #
        # If there is a cycle:
        # slowPointer == fastPointer
        #
        # If fastPointer reaches 1:
        # number is happy

        slowPointer = self.sumOfSquares(n)
        fastPointer = self.sumOfSquares(self.sumOfSquares(n))

        # Continue until:
        # 1. fastPointer becomes 1  -> Happy Number
        # OR
        # 2. slowPointer meets fastPointer -> Cycle detected
        while fastPointer != 1 and slowPointer != fastPointer:

            # Move slow pointer by 1 step
            slowPointer = self.sumOfSquares(slowPointer)

            # Move fast pointer by 2 steps
            fastPointer = self.sumOfSquares(
                self.sumOfSquares(fastPointer)
            )

        # If fastPointer reaches 1,
        # the number is happy
        if fastPointer == 1:
            return True
        else:
            return False


    def sumOfSquares(self, n):

        # This function calculates:
        # sum of squares of digits of n
        #
        # Example:
        # n = 19
        # 1^2 + 9^2 = 82

        sum = 0

        while n > 0:

            # Get last digit
            digit = n % 10

            # Add square of digit
            sum = sum + (digit ** 2)

            # Remove last digit
            n = n // 10

        return sum