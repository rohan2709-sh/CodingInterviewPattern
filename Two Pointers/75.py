"""
✅ Dutch National Flag Algorithm (Sort 0s, 1s, 2s)

Goal:
- Sort the array so that all 0s come first, then 1s, then 2s.

Pointers:
- start   -> index where next 0 should be placed (initially 0)
- current -> scans the array (initially 0)
- end     -> index where next 2 should be placed (initially last index)

Loop:
- Continue while current <= end

Cases:
1) If colors[current] == 0:
   - Swap colors[current] and colors[start]  (move 0 to beginning)
   - start += 1
   - current += 1

2) If colors[current] == 1:
   - 1 is already in the correct middle section
   - current += 1

3) If colors[current] == 2:
   - Swap colors[current] and colors[end] (move 2 to end)
   - end -= 1
   - DO NOT increment current (check swapped value again)
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        end = len(nums) - 1
        current = 0
        while current <= end:
            if nums[current] == 0:
                temp = nums[start]
                nums[start] = nums[current]
                nums[current] = temp
                start += 1
                current += 1
            elif nums[current] == 2:
                temp = nums[end]
                nums[end] = nums[current]
                nums[current] = temp
                end -= 1
    
            else:
                current += 1
        
        