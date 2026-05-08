 # Time Complexity: O(n log n) — sorting dominates; the two-pointer scan is O(n)
  # Space Complexity: O(1) — no extra data structures, sorting is done in-place                                                                                   
                                                                                                                                                                  
    class Solution:                                           
      def twoSumLessThanK(self, nums: List[int], k: int) -> int:

          # Sort the array so we can reason about sums directionally.
          # With sorted order, moving 'left' right increases the sum,
          # and moving 'right' left decreases it.                                                                                                                 
          nums.sort()
                                                                                                                                                                  
          # Start with one pointer at each end of the sorted array.
          left = 0
          right = len(nums) - 1                                                                                                                                   
   
          # Track the best (largest) valid sum found so far.                                                                                                      
          # -1 is the sentinel value for "no valid pair found".
          result = -1

          # Move the pointers toward each other until they meet.                                                                                                  
          while left < right:
                                                                                                                                                                  
              current_sum = nums[left] + nums[right]        

              if current_sum < k:
                  # KEY INSIGHT:
                  # This pair is valid (sum < k). Update result if this sum
                  # is better than what we've seen so far.                                                                                                        
                  # Then move 'left' rightward to try a larger sum —
                  # a larger sum that still stays under k would be even better.                                                                                   
                  result = max(result, current_sum)         
                  left += 1                                                                                                                                       
              else:
                  # The sum is too large (>= k), so it's invalid.                                                                                                 
                  # Move 'right' leftward to bring the sum down.
                  right -= 1
                                                                                                                                                                  
          return result