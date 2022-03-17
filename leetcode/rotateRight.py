# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==0 or head==None: return head
        curr = head
        cnt = 0
        while curr!=None:
            cnt += 1
            curr = curr.next
        k %= cnt
        target = cnt - k
        answer = ListNode()
        ans = answer
        curr = head
        for i in range(target):            
            curr = curr.next
        while curr!=None:
            answer.next = ListNode()
            answer = answer.next
            answer.val = curr.val
            curr = curr.next
        curr = head
        for i in range(target):
            answer.next = ListNode()
            answer = answer.next
            answer.val = curr.val
            curr = curr.next
        return ans.next
