class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = set()
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        cnt = len(dic)
        res = 0
        for i in range(len(s)):
            dic[s[i]] -= 1
            if dic[s[i]] == 0:
                cnt -= 1
            left.add(s[i])
            if len(left) == cnt:
                res += 1
        return res