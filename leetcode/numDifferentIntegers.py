class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        answer = set()
        idx = 0
        num = ''
        while idx < len(word):
            if word[idx].isdigit():
                num += word[idx]
            else:
                if num!='':
                    answer.add(int(num))
                    num = ''
            idx += 1
        if num!='': answer.add(int(num))
        return len(answer)
            
                