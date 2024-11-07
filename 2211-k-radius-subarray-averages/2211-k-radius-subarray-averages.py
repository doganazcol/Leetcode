class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        avgs = [-1] * n  # Initialize result array with -1
        if n < 2 * k + 1:
            return avgs  # If there aren't enough elements for any k-radius average
        
        # Step 1: Calculate prefix sums
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        # Step 2: Compute the k-radius averages
        for i in range(k, n - k):
            left = i - k
            right = i + k
            subarray_sum = prefix_sums[right + 1] - prefix_sums[left]  # Sum from left to right
            avgs[i] = subarray_sum // (2 * k + 1)  # Average using integer division
        
        return avgs