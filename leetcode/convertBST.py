# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, val):
            if not node: return 0
            r = dfs(node.right,val)
            orig, node.val = node.val, node.val + val + r
            l = dfs(node.left, node.val)
            return r + orig + l
        dfs(root,0)
        return root