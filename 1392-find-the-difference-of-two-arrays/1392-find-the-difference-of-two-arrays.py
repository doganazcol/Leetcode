class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        #input: nums1, nums2
        #output: lst(answer) : size -> 2
        #array: same type, fixed size 
        #list: diff type, mutable size
        
        #alg
        #1. convert to set 
        #2. compare while reconverting to list
        #3. return 

        #1
        list1 = set(nums1)
        list2 = set(nums2)

        #2
        answer1 = list(list1 - list2)
        answer2 = list(list2 - list1)

        #3
        return [answer1, answer2]

