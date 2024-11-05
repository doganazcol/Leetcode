class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """ 
        #1
        i  = j = 0
        ans = []

        #2
        while i < len(s) and j < len(s): 
            #condition
            for i in range(k * 2):
                for i in range(k):
                    temp = s[i]
                    s[i + 1] = s[i]
                    s[i] = temp
        return s
            #increment pointers 3 
        """
        """ s = list(s)
    
    # Process each 2k segment
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters within the current 2k segment
            left, right = i, min(i + k - 1, len(s) - 1)
            
            # Swap characters using two pointers
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        # Join the list back to a string and return
        return ''.join(s)   
        """
        ans = []
        i = 0  # Initialize index for traversing the string

        # Process the string in chunks of 2k
        while i < len(s):
            # Get the next 2k characters (or as many as remain)
            chunk = s[i:i + 2 * k]
            
            # Reverse the first k characters in the chunk
            reversed_part = chunk[:k][::-1]
            remaining_part = chunk[k:]
            
            # Add the processed chunk to the answer
            ans.append(reversed_part + remaining_part)
            
            # Move to the next 2k segment
            i += 2 * k

        # Join all parts and return the result
        return ''.join(ans)




