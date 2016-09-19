class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inorder_helper(root)[k-1]
    
    def inorder_helper(self, root):
        if root == None:
            return []
        return self.inorder_helper(root.left) + [root.val] + self.inorder_helper(root.right)