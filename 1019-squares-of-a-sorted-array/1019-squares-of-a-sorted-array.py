class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        # Initialize a result array with the same length, filled with zeros
        result = [0] * len(nums)
        # Fill result from the end to the beginning
        position = len(nums) - 1

        while l <= r:
            left_square = nums[l] ** 2
            right_square = nums[r] ** 2

            #manuel sort
            if left_square > right_square:
                result[position] = left_square
                l += 1
            else:
                result[position] = right_square
                r -= 1
            position -= 1

        return result