# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node: #if empty
                return 0
            
            #check the current node
            good = 1 if node.val >= max_val else 0

            #updating the values 
            new_max = max(max_val, node.val)

            #recursion
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)

            return good 
        return dfs(root, root.val if root else float('inf'))

