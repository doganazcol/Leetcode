class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #subarray with constraint = sliding window 


        if k<= 1: 
            return 0

        #variable definitiom
        ans = left = 0 
        cur = 1 # since doing products 

        for right in range(len(nums)):
            cur *= nums[right] # add to current window the products 
            
            #constraint 
            while cur >= k: 
                cur //=nums[left] #reverse product
                left += 1
            
            ans += right - left + 1
        return ans

