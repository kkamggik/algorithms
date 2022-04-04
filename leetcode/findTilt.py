# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = 0
        def dfs(root):
            global res
            if root==None: return 0
            leftnode = dfs(root.left)
            rightnode = dfs(root.right)
            res += abs(leftnode-rightnode)
            return leftnode+rightnode+root.val
        dfs(root)
        return res
        