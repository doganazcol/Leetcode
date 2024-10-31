class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()  # Set to keep track of characters in the current substring
        l = 0  # Left pointer of the sliding window
        res = 0  # To store the maximum length of substring without duplicates

        for r in range(len(s)):
            # If we find a duplicate, adjust the left pointer until there are no duplicates
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Add the current character to the set
            charSet.add(s[r])
            # Update the maximum length found
            res = max(res, r - l + 1)
        
        return res
        