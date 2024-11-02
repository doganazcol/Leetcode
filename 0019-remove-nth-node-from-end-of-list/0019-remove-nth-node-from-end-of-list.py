# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)

        #acts as indexes
        left  = dummy
        right = head

        #cant do with a caclculation since both pointers are dynamically changing
        #r =  head + n 

        while n > 0 and right is not None: 
            right = right.next 

            #when n = 0, that means that the space between them are the wanted value
            n -=1 

        while right: 
            left = left.next 
            right = right.next 
        
        #delete 
        left.next = left.next.next 

        return dummy.next

