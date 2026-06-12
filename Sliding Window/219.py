# We use the Sliding Window technique because we only care about
# duplicates whose indices differ by at most k.
#
# 1. Maintain a window containing the last k elements using a set.
#
# 2. For each number:
#    - If it already exists in the window, we found a duplicate
#      within distance k, so return True.
#    - Otherwise, add it to the window.
#
# 3. If the window grows beyond size k:
#    - Remove the element that falls out of the allowed range
#      (nums[i - k]).
#
# 4. If we finish iterating without finding a duplicate,
#    return False.
#
# Example:
# nums = [1,2,3,1], k = 3
#
# i = 0, window = {}
# 1 not in window -> add 1
# window = {1}
#
# i = 1, window = {1}
# 2 not in window -> add 2
# window = {1,2}
#
# i = 2, window = {1,2}
# 3 not in window -> add 3
# window = {1,2,3}
#
# i = 3, window = {1,2,3}
# 1 already exists in window
# return True
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mySet = set()
        for i in range(0, len(nums)):
            if nums[i] in mySet:
                return True
            mySet.add(nums[i])
            if len(mySet) > k:
                mySet.remove(nums[i - k])
        return False
