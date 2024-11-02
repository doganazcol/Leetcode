# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #RECURSION
        #DFS - depth first search 

        #base == root is empty 
        if not root: 
            return None

        #swap
        temp = root.left 
        root.left = root.right  
        root.right = temp 

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

