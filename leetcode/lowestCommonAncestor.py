# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        global ans
        ans = None
        self.check(root, p, q)
        return ans
        
    def check(self, node, p, q):
        if not node: return False
        l = self.check(node.left, p, q)
        r = self.check(node.right, p, q)
        mid = node == p or node == q
        if l + r + mid >= 2:
            global ans
            ans = node
        return l or r or mid
