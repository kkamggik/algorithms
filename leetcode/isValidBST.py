class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def dfs(self, node):
        global answer
        value = node.val
        if node.left != None:
            if node.left.val < value:
                self.dfs(node.left)
            else: 
                answer = False
                return
        if node.right != None:
            if node.right.val > value:
                self.dfs(node.right)
            else:
                answer = False
                return
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        global answer
        answer = True
        self.dfs(root)
        print(answer)
head = TreeNode()
curr = head
curr.val = 2
curr.left = TreeNode(1)
curr.right = TreeNode(3)
sol = Solution()
sol.isValidBST(head)
