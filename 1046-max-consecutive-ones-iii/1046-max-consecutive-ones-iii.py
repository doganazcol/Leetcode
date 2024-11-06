class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_length = 0
        zeros_count = 0

        # Iterate through the array with the right pointer
        for right in range(len(nums)):
            # If the current element is 0, increment zeros_count
            if nums[right] == 0:
                zeros_count += 1

            # If zeros_count exceeds k, move the left pointer to the right
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            # Calculate the max length of the subarray
            max_length = max(max_length, right - left + 1)

        return max_length