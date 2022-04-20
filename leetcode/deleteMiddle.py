# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cnt = 0
        curr = head
        while curr!=None:
            cnt += 1
            curr = curr.next
        if cnt == 1: return None
        target = (cnt//2)-1
        curr = head
        for i in range(target):
            curr = curr.next
        curr.next = curr.next.next
        return head