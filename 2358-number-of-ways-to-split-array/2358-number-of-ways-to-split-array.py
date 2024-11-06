class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #prefix array initialization
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        # Total sum of all elements in nums
        total_sum = prefix[-1]
        
        # Step 2: Count valid splits
        count = 0
        for i in range(len(nums) - 1):
            # Left sum is prefix[i], right sum is total_sum - prefix[i]
            if prefix[i] >= total_sum - prefix[i]:
                count += 1
        
        return count 
