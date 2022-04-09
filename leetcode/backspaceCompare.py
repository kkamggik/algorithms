class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        idx1 = idx2 = 0
        while idx1<len(s):
            if s[idx1]!='#': stack1.append(s[idx1])
            elif stack1: stack1.pop()
            idx1 += 1
        while idx2<len(t):
            if t[idx2]!='#': stack2.append(t[idx2])
            elif stack2: stack2.pop()
            idx2 += 1
        return stack1==stack2