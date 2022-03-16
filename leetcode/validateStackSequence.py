class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        n = len(pushed)
        stack = []
        idx = 0
        for p in pushed:
            stack.append(p)
            while stack and stack[-1]==popped[idx]:
                stack.pop()
                idx += 1
        if not stack: return True
        return False