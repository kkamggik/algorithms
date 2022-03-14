"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copydict = {None: None}
        curr = head
        while curr!=None:
            copydict[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        while curr:
            if curr.next:
                copydict[curr].next = copydict[curr.next]
            if curr.random:
                copydict[curr].random = copydict[curr.random]
            curr = curr.next
        return copydict[head]
            