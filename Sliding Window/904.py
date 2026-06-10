# We use the Sliding Window technique because we need to find
# the longest contiguous subarray that contains at most 2 distinct fruit types.
#
# 1. Maintain a frequency map (fruitMap) for the current window.
#
# 2. Expand the window by moving 'i' and adding fruits[i] into fruitMap.
#
# 3. If the window contains more than 2 distinct fruit types:
#    - The window becomes invalid.
#    - We must shrink it from the left using 'start'.
#
# 4. Shrinking process:
#    - Decrease frequency of fruits[start] in the map.
#    - If frequency becomes 0, remove that fruit type from the map.
#    - Move start forward to reduce window size.
#
# 5. After each valid window, calculate its size (i - start + 1)
#    and update the maximum fruits collected.
#
# 6. Continue until the end of the array.
#
# 7. Return the maximum window size found.
#
# Example:
# fruits = [1,2,3,2,2]
#
# Window [1]
# Types = {1}
# Max = 1
#
# Window [1,2]
# Types = {1,2}
# Max = 2
#
# Window [1,2,3] -> invalid (3 types)
#
# Shrink:
# Remove 1 → [2,3]
# Still 2 types
#
# Window [2,3]
# Max = 2
#
# Window [2,3,2]
# Types = {2,3}
# Max = 3
#
# Window [2,3,2,2]
# Types = {2,3}
# Max = 4
#
# Answer = 4
#
# Time Complexity: O(n)
# Space Complexity: O(1)  # at most 2 fruit types in window
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitMap = dict()
        start = 0
        maxFruits = 0
        for i in range(0, len(fruits)):
            if len(fruitMap) == 2 and not fruits[i] in fruitMap:
                maxFruits = max(maxFruits, sum(fruitMap.values()))
                while len(fruitMap) == 2 and fruits[start] in fruitMap:
                    fruitMap[fruits[start]] = fruitMap.get(fruits[start]) - 1
                    if fruitMap[fruits[start]] == 0:
                        fruitMap.pop(fruits[start])
                    start += 1
            fruitMap[fruits[i]] = fruitMap.setdefault(fruits[i], 0) + 1
        maxFruits = max(maxFruits, sum(fruitMap.values()))
        return maxFruits
