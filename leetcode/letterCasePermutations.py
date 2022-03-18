class Solution(object):
    def permutation(self, idx, curr, s):
        if len(curr)==len(s):
            global answer
            answer.append(str(curr))
            return 
        if s[idx].isalpha():
            self.permutation(idx+1, curr+s[idx].lower(), s)
            self.permutation(idx+1, curr+s[idx].upper(), s)
        else:
            self.permutation(idx+1, curr+s[idx], s)
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        global answer
        answer = []
        self.permutation(0,'',s)
        return answer