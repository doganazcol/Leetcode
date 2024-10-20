# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Handle the case when the list is empty
        if not head:
            return None  
        
        p1 = head
        p2 = head.next
        
        while p2:
            # Compare values, not the node objects
            
            #1->2->2->2->3
            if p1.val == p2.val:
                p1.next = p2.next  # Skip the duplicate
            
            
            else:
                p1 = p1.next  # Move p1 to the next node only when no duplicate is found
            
            # Move p2 to the next node in all cases
            #if there is multiple duplicates, this line handles that case
            
            p2 = p2.next
            
        return head  
                
                
                
                
                
        