# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        def visit(node):
            if not node: return
            arr.append(node.val)
            visit(node.left)
            visit(node.right)
        visit(root)
        arr.sort()
        head = TreeNode()
        curr = head
        for n in arr:
            new = TreeNode()
            new.val = n
            curr.right = new
            curr = curr.right
        return head.right
            
            