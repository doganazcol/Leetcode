class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #initialize
        l = 0 
        r = len(s) - 1

        while l < r: 

            #reverse



            s[l], s[r] = s[r], s[l]
            
            #temp = s[r] 
            #s[r] = s[l]
            #s[l] = temp

            #update opinters
            l += 1
            r -= 1

        return s

        """ #in place s[:]
        s[:] = list(reversed(s))
        return s """


