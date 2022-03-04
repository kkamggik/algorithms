# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        curr = head
        while curr!=None:
            nums.append(curr.val)
            curr = curr.next
        nums.reverse()
        head = ListNode()
        answer = head
        for n in nums:
            answer.next = ListNode()
            answer = answer.next
            answer.val = n
        return head.next