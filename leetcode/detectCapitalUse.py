class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word1 = word.upper()
        word2 = word.lower()
        word3 = word.capitalize()
        return True if word in [word1,word2,word3] else False