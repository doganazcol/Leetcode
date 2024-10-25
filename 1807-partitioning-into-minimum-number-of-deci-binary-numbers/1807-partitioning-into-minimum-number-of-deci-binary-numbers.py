class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        """ #ASCII values 0 = 48, 9 = 57 

        answer = 0
        #print(list(n))

        for character in n: 
            current = ord(character) - 48
            answer = max(current, answer)

        return answer  """

       # print(max(n))


       #If you do max(n) where n is a string of digits, 
       #it will return the character with the highest lexicographical (dictionary) value
        return int(max(n))


