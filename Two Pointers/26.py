class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        Explanation

        We use the Two Pointer approach.

        p1 -> points to the position where the next unique element
              should be placed.

        p2 -> traverses the array to find new unique elements.

        Since the array is already sorted:
        - Duplicate elements will always appear next to each other.
        - We only need to compare nums[p1] and nums[p2].

        Initial State:
        p1 = 0
        p2 = 0
        uniqueElements = 1

        Example:
        nums = [0,0,1,1,1,2,2,3,3,4]

        Step-by-step:

        p1 = 0, p2 = 0
        nums[p1] == nums[p2]
        -> duplicate, move p2

        p1 = 0, p2 = 1
        nums[p1] == nums[p2]
        -> duplicate, move p2

        p1 = 0, p2 = 2
        nums[p1] != nums[p2]
        -> found a new unique element

        Move p1 forward:
        p1 = 1

        Place new unique element at nums[p1]:
        nums[1] = nums[2]

        Array becomes:
        [0,1,1,1,1,2,2,3,3,4]

        Increase uniqueElements count.

        Continue this process until p2 reaches the end.

        Final array:
        [0,1,2,3,4,_,_,_,_,_]

        Time Complexity:
        O(n) -> each element is visited once

        Space Complexity:
        O(1) -> in-place modification
        """

        p1 = 0
        p2 = 0
        uniqueElements = 1

        while p2 < len(nums):

            if nums[p1] != nums[p2]:

                p1 += 1
                nums[p1] = nums[p2]

                uniqueElements += 1

            p2 += 1

        return uniqueElements