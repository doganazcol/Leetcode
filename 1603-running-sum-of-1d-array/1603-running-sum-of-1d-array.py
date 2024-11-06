class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
    #BUILD PREFIX !! ALGORITHM
        prefix = [nums[0]]
        #answer.append(prefix)

        #BUILDING SUM
        for i in range(1, len(nums)):  
            prefix.append(nums[i] + prefix[-1])
            #answer.append(i)
        

        #CUSTOMIZE - leap of faith
        answer = []

        for i in range(len(nums)):
            answer.append(prefix[i])

        return answer