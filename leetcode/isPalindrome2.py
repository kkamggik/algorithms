# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        lst = []
        while curr!=None:
            lst.append(curr.val)
            curr = curr.next
        mid = len(lst)//2
        if len(lst)%2==0:
            return lst[:mid] == lst[mid:][::-1]
        else:
            return lst[:mid] == lst[mid+1:][::-1]
            