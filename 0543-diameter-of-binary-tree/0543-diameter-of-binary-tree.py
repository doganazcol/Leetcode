# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #global variable 
        res = 0 

        #returns height - helper function
        #represents the current node being processed.
        def dfs(curr): 

            #curr is None (indicating we've reached a leaf node's child
            if not curr: 
                return 0
            
            #recursion
            left = dfs(curr.left)
            right = dfs(curr.right)

            global res
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res