class Solution(object):
    def check(self, s, start, end):
        while start < end:
            if s[start]!=s[end]: return False
            start += 1
            end -= 1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start,end = 0,len(s)-1
        while start < end:
            if s[start]!=s[end]:
                return self.check(s,start+1,end) or self.check(s,start,end-1)
            start += 1 
            end -= 1    
        return True