class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = ans = cur = 0 

        #first window sum
        for right in range(k): 
            cur += nums[right] 

        ans = float(cur) / k

        #broken pipe 
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i -k]  #update the window
            ans = max(float(cur)/ k, ans)
       

        return ans

