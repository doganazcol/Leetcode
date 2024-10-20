class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        #MISTAKES 
        #1.CONVERT INT TO STRING 
        #2. LEN(ARRAY) NOT LEN? // GETTING LEN OF WHAT
        #3. LEFT SHOULD BE SMALLER THAN RIGHT 
        
        #make it string to operate on
        x_str = str(x)


        #assign pointers to indexez

        left = 0
        right = len(x_str) - 1

        #palindromic struct  
        while left < right:
            if x_str[left] != x_str[right]:
                return False
            #should not be in the same indentation level of "return False"
            # because it quits the code 
           
            #updated when they are equal 
            left += 1
            right -= 1
        # executed after all while loop elements are checked
        return True

        


        