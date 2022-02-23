# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answer = ListNode()
        head = answer
        remainder = 0
        while l1!=None or l2!=None:
            a,b = 0,0
            if l1!=None:
                a = l1.val
                l1 = l1.next
            if l2!=None:
                b = l2.val
                l2 = l2.next
            add = a+b+remainder
            remainder = add//10
            left = add%10
            answer.next = ListNode(left)
            answer = answer.next
        if remainder:
            answer.next = ListNode(remainder)
        return head.next  