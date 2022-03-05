from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None: return []
        answer = []
        queue = deque()
        queue.append(root)
        while queue:
            ans,size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                ans.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            answer.append(ans)
        for i in range(1,len(answer),2):
            answer[i] = answer[i][::-1]
        return answer