class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            if stack[-1][1] == k: stack.pop()
        res = ''
        for c,f in stack:
            res += (c*f)
        return res