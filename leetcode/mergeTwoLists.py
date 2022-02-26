# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        answer = ListNode()
        head = answer
        while list1!=None or list2!=None:
            if (list1!=None and list2!=None and list1.val < list2.val) or (list1!=None and list2==None):
                answer.next = ListNode()
                answer = answer.next
                answer.val = list1.val
                list1 = list1.next
            elif (list1!=None and list2!=None and list1.val >= list2.val) or (list2!=None and list1==None):
                answer.next = ListNode()
                answer = answer.next
                answer.val = list2.val
                list2 = list2.next
        return head.next
                