class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        dic = {}
        for word in words:
            for w in word:
                if w not in dic: dic[w] = 1
                else: dic[w] += 1
        n = len(words)
        for k,v in dic.items():
            if v%n != 0:
                return False
        return True