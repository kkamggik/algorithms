class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="": return True
        idx = 0
        for i in range(len(t)):
            if t[i]==s[idx]:
                idx += 1
            if idx == len(s): return True
        return False