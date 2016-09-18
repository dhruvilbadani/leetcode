# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid_BST_helper(root, float("-inf"), float("inf"))
    
    def is_valid_BST_helper(self, root, min_val, max_val):
        if root == None:
            return True
        return root.val > min_val and root.val < max_val and self.is_valid_BST_helper(root.left, min_val, root.val) and self.is_valid_BST_helper(root.right, root.val, max_val)