class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        a = b = res = 0
        for c in firstWord:
            a *= 10
            a += ord(c)-97
        for c in secondWord:
            b *= 10
            b += ord(c)-97
        for c in targetWord:
            res *= 10
            res += ord(c)-97
        return a+b == res