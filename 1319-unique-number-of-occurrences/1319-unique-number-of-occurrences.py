class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)

        occurence = Counter(arr)
        print(occurence)
        
        #frequency = Counter([v for v in occurence.values()])
        frequency = [v for v in occurence.values()]
        #print(frequency)
        
        unique = list(set(frequency))
        len_u = len(unique)
        len_f = len(frequency)

        #frequency works
        if len_u == len_f:
            return True
        return False