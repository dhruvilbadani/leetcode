class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root ==  None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]