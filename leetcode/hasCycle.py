# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dic = {}
        curr = head
        while curr!=None:
            if curr not in dic: dic[curr] = True
            else: return True
            curr = curr.next
        return False