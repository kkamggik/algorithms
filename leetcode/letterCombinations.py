class Solution(object):
    def possible(self, idx, word, digits):
        global nums
        if idx == len(digits):
            global answer
            if word!='': answer.append(word)
            return
        for c in nums[digits[idx]]:
            self.possible(idx+1, word+c,digits)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        global nums,answer
        nums = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"], "5": ["j","k","l"], "6": ["m","n","o"], "7": ["p","q","r",

"s"], "8": ["t","u","v"], "9": ["w","x","y","z"] }
        answer = []
        self.possible(0,'',digits)
        return answer