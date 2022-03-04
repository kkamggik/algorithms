# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):        
    def check(self, l, r):
        if not l and not r: return True
        if l and r and l.val==r.val:
            return self.check(l.left, r.right) and self.check(l.right, r.left)
        return False     
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        answer = self.check(root,root)
        return answer