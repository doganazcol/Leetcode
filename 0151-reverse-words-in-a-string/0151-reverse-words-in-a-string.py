class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #print(s.split())
        new_s = s.split()
        right = len(new_s) - 1
        
        res, i = [], 0 
        while i < len(s) and right >= 0: 
                res.append(new_s[right])
                if right > 0: 
                    res.append(' ')
                #res.append(' ')
                right -= 1
            #print(res)
        return str(''.join(res))
