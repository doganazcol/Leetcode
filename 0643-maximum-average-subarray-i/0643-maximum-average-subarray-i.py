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

 
        """ 
        cur = sum(nums[:k])
        ans = cur / k  # Initialize ans with the average of the first window

        # Slide the window across the array
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]  # Update the window sum by sliding it
            ans = max(ans, cur / k)  # Calculate the average of the current window and update ans if it's higher

        return ans 
        """