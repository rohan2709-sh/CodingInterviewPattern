class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        for i in range(len(nums) - 2):
            # Since the array is sorted if the current number is zero that means
            # all the numbers to the right will b positive so there sum will be greater than zero
            # Hence break the loop
            if nums[i] > 0:
                break
            #To Avoid duplicates
            if i == 0 or (nums[i] != nums[i - 1]):
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum < 0:
                        left += 1
                    elif sum > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Since no duplicates are allowed skip the left and right elements if they are equal to the previous values
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result
