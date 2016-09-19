# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_height = self.get_left_height(root.left)
        right_height = self.get_right_height(root.right)
        if left_height == right_height:
            return 2**(left_height+1) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def get_left_height(self, root):
        tmp = root
        height = 0
        while tmp != None:
            tmp = tmp.left
            height += 1
        return height
    
    def get_right_height(self, root):
        tmp = root
        height = 0
        while tmp != None:
            tmp = tmp.right
            height += 1
        return height