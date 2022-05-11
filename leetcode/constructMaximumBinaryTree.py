# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        idx = nums.index(max(nums))
        node = TreeNode(nums[idx])
        node.left = self.constructMaximumBinaryTree(nums[:idx])
        node.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return node
        