class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        """    
        length = len(digits)
        #integer = array
        #increment last elemnt by 1 
        digits[length - 1] = digits[length - 1] + 1
        
        #edge case [9, 9 , 9] = [1, 0, 0, 0]
        empty = []
        if digits[length - 1] == 9:
            for i in range(length + 1):
                with append you'll get a nested list rather than individual elements added.
               empty.add("0")
               empty[0] = 1
               i += 1

        #return resulting array of didgits 
        else:
            return digits """

        length = len(digits)
        
        # Increment the last element by 1
        digits[length - 1] += 1
        
        # Edge case: Handle [9, 9, 9] where it results in [1, 0, 0, 0]
        for i in range(length - 1, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i > 0:
                    digits[i - 1] += 1
                else:
                    digits = [1] + digits
        
        return digits