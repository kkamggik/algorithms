# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        ans = ListNode()
        answer = ans
        while curr != None:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
            else:
                ans.next = ListNode()
                ans = ans.next
                ans.val = curr.val
            curr = curr.next
        return answer.next
                