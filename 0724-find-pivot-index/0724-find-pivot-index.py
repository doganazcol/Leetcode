class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)  # Total sum of the array
        left = 0  # Initialize left sum
        
        for i in range(len(nums)):  # Iterate over the array
            # Check if left sum equals right sum
            if left == total - left - nums[i]:
                return i  # Return index if the condition is satisfied
            
            left += nums[i]  # Update the left sum by adding the current element
        
        return -1  # If no pivot index is found, return -1
