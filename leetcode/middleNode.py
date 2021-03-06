# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle = 0
        curr = head
        while curr!=None:
            curr = curr.next
            middle += 1
        middle//=2
        curr = head
        for i in range(middle):
            curr = curr.next
        return curr