# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        dic = {}
        curr = head
        while curr!=None:
            if curr not in dic:
                dic[curr] = True
            else: return curr
            curr = curr.next
        return None