class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            elif c == '}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else: return False
            elif c == ']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else: return False
            elif c == ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else: return False
        if not stack: return True
        return False