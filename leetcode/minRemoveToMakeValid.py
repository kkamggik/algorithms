class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        check = [1]*len(s)
        stack = []
        for idx,c in enumerate(s):
            if c.isalpha(): continue
            elif c=='(':
                stack.append(idx)
            elif c==')':
                if not stack: check[idx] = 0
                elif s[stack[-1]]=='(': stack.pop()
        while stack:
            idx = stack.pop()
            check[idx] = 0
        answer = ''
        for i in range(len(s)):
            if check[i]==1:
                answer += s[i]
        return answer
                