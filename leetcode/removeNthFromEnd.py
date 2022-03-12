# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        idx = 0
        while curr != None:
            idx += 1
            curr = curr.next
        target = idx - n - 1
        if target < 0: return head.next
        curr = head
        for i in range(target):
            curr = curr.next
        curr.next = curr.next.next
        return head
            