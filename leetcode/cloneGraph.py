"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        queue = deque()
        queue.append(node)
        nodes = {node.val: Node(node.val, [])}
        while queue:
            n = queue.popleft()
            clone = nodes[n.val]
            for nxt in n.neighbors:
                if nxt.val not in nodes:
                    nodes[nxt.val] = Node(nxt.val, [])
                    queue.append(nxt)
                clone.neighbors.append(nodes[nxt.val])
        return nodes[node.val]