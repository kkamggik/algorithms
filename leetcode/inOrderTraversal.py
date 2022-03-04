# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,node):
        if node == None: return
        global answer
        self.inorder(node.left)
        answer.append(node.val)
        self.inorder(node.right)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        global answer
        answer = []
        self.inorder(root)
        return answer