# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None: return []
        rst = []
        queue = deque()
        queue.append(root)
        rst.append(root.val)
        while queue:
            s = len(queue)
            for _ in range(s):
                node = queue.popleft()
                if node.left:queue.append(node.left)
                if node.right: queue.append(node.right)
            if queue: rst.append(queue[-1].val)
        return rst