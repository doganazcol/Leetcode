class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # base 
        if len(s) != len(t):
            return False

        #empty hash
        hashMapS, hashMapT = {}, {}

        #key value matching
        for i in range(len(s)):
            hashMapS[s[i]] = 1 + hashMapS.get(s[i],0)
            hashMapT[t[i]] = 1 + hashMapT.get(t[i],0)
        
        for c in hashMapS:
            if hashMapS[c] != hashMapT.get(c, 0):
                return False
        return True



