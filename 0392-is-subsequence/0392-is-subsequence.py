class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        si = tj = 0 

        answer = 0 

        #pointer out of bounds 
        while si < len(s) and tj < len(t) and len(s) < len(t):
            if  s[si] == t[tj]:
                si += 1
            tj += 1
        return len(s) == si

