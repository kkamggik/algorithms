class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        def check(alp1,alp2):
            for i in range(26):
                if alp1[i]!=alp2[i]: return False
            return True
        res = []
        if len(s) < len(p): return res
        alp = [0]*26
        for c in p:
            alp[ord(c)-97] += 1
        alp2 = [0]*26
        start = 0
        for i in range(len(s)):
            if i < len(p):
                alp2[ord(s[i])-97] += 1
            else:
                alp2[ord(s[i])-97] += 1
                alp2[ord(s[start])-97] -= 1
                start += 1
            if check(alp,alp2): res.append(i-len(p)+1)
        return res
        