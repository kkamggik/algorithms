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
        curr = head
        if target == -1:
            head = curr.next
        else:
            idx = 0
            while curr != None:
                if idx == target:
                    curr.next = curr.next.next
                    break
                curr = curr.next
                idx += 1
        curr = head
        answer = ListNode()
        head = answer
        while curr!=None:
            answer.next = ListNode()
            answer = answer.next
            answer.val = curr.val
            curr = curr.next
        return head.next
            