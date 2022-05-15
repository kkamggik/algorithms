# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = defaultdict(list)
        global deep
        deep = 0
        def deepest(root,idx):
            if root.left: deepest(root.left, idx+1)
            if root.left == None and root.right == None:
                values[idx].append(root.val)
                global deep
                deep = max(deep, idx)
            if root.right: deepest(root.right, idx+1)
        deepest(root,0)
        return sum(values[deep])

