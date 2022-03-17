class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                x = stack.pop()
                stack[-1] += max(2*x, 1)
        return stack.pop()