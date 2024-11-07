class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Create a set of all numbers from 0 to n
        full_set = set(range(n + 1))
        
        # Step 2: Convert nums to a set
        nums_set = set(nums)
        
        # Step 3: Find the missing number by checking the difference
        missing_number = full_set - nums_set  # This will give a set with one missing element
        
        return missing_number.pop()  # Extract the single element from the set

            