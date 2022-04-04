# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr = head
        for i in range(1,k):
            curr = curr.next
        target1 = curr
        total = 0
        curr = head
        while curr!=None:
            curr = curr.next
            total += 1
        if total == 1: return head
        target = total - k
        curr = head
        for i in range(1,target+1):
            curr = curr.next
        target2 = curr
        target1.val, target2.val = target2.val,target1.val    
        return head
        