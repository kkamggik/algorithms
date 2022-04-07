# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        arr = []
        curr = head
        while curr!=None:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        idx = 0
        curr = head
        while curr!=None:
            curr.val = arr[idx]
            idx += 1
            curr = curr.next
        return head