class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Building Prefix Sum
        #Algorithm
        prefix_sum = 0
        min_prefix_sum = 0

        # Iterate through the nums to find the minimum prefix sum
        for num in nums:
            prefix_sum += num
            min_prefix_sum = min(min_prefix_sum, prefix_sum)

        
        startValue = 1 - min_prefix_sum

        return startValue



        