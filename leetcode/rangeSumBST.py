# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        def add(node):
            if not node: return 0
            l = add(node.left)
            r = add(node.right)
            if low <= node.val <= high:
                return node.val + l + r
            else: return l + r
        return add(root)
            