class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # Sort the array so we can use the two-pointer technique.
        # Sorting lets us make decisions based on whether sums are too big or too small.
        nums.sort()
        result = 0
        
        # Fix the first number of the triplet using index i.
        # We stop at len(nums) - 2 because we need at least 2 more numbers after i.
        for i in range(len(nums) - 2):
            
            # Set up two pointers:
            # 'left' starts right after i (the second number of the triplet)
            # 'right' starts at the end of the array (the third number of the triplet)
            left = i + 1
            right = len(nums) - 1
            
            # Move the pointers toward each other until they meet.
            while left < right:
                
                # Calculate the sum of the current triplet.
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < target:
                    # KEY INSIGHT: 
                    #The array is sorted, so nums[right] is the LARGEST
                    #value between left and right. If nums[i] + nums[left] + nums[right]
                    # is already less than target, then pairing nums[left] with ANY value
                    # from index (left+1) up to index (right) will also be less than target.
                    #
                    # That's exactly (right - left) valid triplets we can count at once.
                    # Example: if left=1 and right=3, we count 3-1 = 2 triplets in one step.
                    result += right - left
                    
                    # Now move 'left' forward to try a bigger second number.
                    # We've already counted everything involving the current nums[left].
                    left += 1
                else:
                    # The sum is too big (>= target).
                    # To make the sum smaller, we need a smaller third number,
                    # so move 'right' one step to the left.
                    right -= 1
        
        return result