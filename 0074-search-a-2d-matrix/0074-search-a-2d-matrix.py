class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search to find the correct row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            # Check if the target is within the current row's range
            if target > matrix[row][-1]:  # target is larger than the last element in the row
                top = row + 1
            elif target < matrix[row][0]:  # target is smaller than the first element in the row
                bot = row - 1
            else:
                break  # target is within the range of the current row

        # If no valid row is found, return False
        if not (top <= bot):
            return False

        # Binary search within the row
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:  # target is larger, search right half
                l = m + 1
            elif target < matrix[row][m]:  # target is smaller, search left half
                r = m - 1
            else:
                return True  # target found in the matrix

        return False