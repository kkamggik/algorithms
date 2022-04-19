class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n==1: return s
        res = 0
        ans = ''
        for i in range(n):
            left = right = i
            c = s[i]
            while left>=0 and s[left]==c:
                left -= 1
            while right<n and s[right]==c:
                right += 1
            while left >=0 and right < n and s[left]==s[right]:
                    left -= 1
                    right += 1 
            if res <  right - left - 1:
                res = right - left - 1
                ans = s[left+1:right]
        return ans
                