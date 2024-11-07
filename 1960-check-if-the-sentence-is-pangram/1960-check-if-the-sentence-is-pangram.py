class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        seen = set(sentence)

        for c in seen: 
            if c not in seen:
                seen.add(c)
            else: 
                continue
        if len(seen) == 26: 
            return True 
        return False    
        
     