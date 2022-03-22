class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        answer = ['a']*n
        for i in range(n-1, -1, -1):
            val = min(26, k-i)
            answer[i] = chr(val+97-1)
            k -= val
        return ''.join(answer)