class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''
        for c in s:
            if c.isalpha() or c.isdigit(): string += c.lower()
        for i in range(len(string)//2):
            if string[i]!=string[len(string)-i-1]: return False
        return True