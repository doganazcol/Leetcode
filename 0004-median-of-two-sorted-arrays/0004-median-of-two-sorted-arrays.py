class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #lists 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left_total = (m+n+1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = left_total - i 
            left1  = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]   if i < m else float('inf')
            left2  = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]   if j < n else float('inf')
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                hi = i - 1
            else:
                lo = i + 1

