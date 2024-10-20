class Solution(object):
    from collections import Counter

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        #they exist
        e1 = Counter(word1)
        e2 = Counter(word2)
        print(e1, e2)
        
        #their frequency should match 
        # loop = frequency 
        fr1 = Counter([v for v in e1.values()])
        fr2 = Counter([v for v in e2.values()])

        return e1 == e2 or (fr1 == fr2 and set(word1) == set(word2))