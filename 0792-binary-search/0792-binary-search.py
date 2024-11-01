class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2  # Calculate the middle index
            
            if nums[m] > target:
                r = m - 1  # Target is in the left half, adjust the right pointer
            elif nums[m] < target:
                l = m + 1  # Target is in the right half, adjust the left pointer
            else:
                return m  # Target found, return the index
        
        return -1  # Target not found in the list