# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Gives hints in return types and input types 
        
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # a dummy node to which we attach nodes from lists.
        # default value of 0 and no next node (next=None).
        
        #cur is a pointer that will traverse the merged list as new nodes are added.
        cur = dummy = ListNode()


        #We iterate over lists using two-pointers
        #not None

        #It means the loop will run until one of the lists is completely traversed.

        #handels the unequal lengths
        while list1 and list2:   

            #index into the linked lists to get the values
            # current node comparison
            
            if list1.val < list2.val:    
                cur.next = list1
                list1, cur = list1.next, list1          
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        #is there anything left after merging

        #remaining nodes after while loop (one list comes to an end)
        # are handled here
        if list1 or list2:
            #if list1 is NOT empty, cur.next = list1
            # if list1 is empty, cur.next = list2
            cur.next = list1 if list1 else list2
            
        return dummy.next