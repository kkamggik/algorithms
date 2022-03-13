# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if curr == None: return head
        prev = head
        curr = curr.next
        idx = 2
        while curr!=None:
            if idx%2==0:
                val = curr.val
                curr.val = prev.val
                prev.val = val
            idx += 1
            prev = prev.next
            curr = curr.next
        return head