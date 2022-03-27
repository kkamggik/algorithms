class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        alp1 = [0]*26
        alp2 = [0]*26
        for c in s:
            alp1[ord(c)-97] += 1
        for c in t:
            alp2[ord(c)-97] += 1
        res = 0
        for i in range(26):
            res += max(alp1[i],alp2[i]) - min(alp1[i],alp2[i])
        return res
            