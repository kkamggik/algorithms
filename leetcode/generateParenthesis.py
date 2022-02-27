class Solution(object):
    def check(self, word):
        stack = []
        for c in word:
            if c == '(':
                stack.append('(')
            else:
                if stack and stack[-1]=='(':
                    stack.pop()
                else: return False
        if stack: return False
        return True
    def dfs(self, idx, n, word, parenthesis):
        if idx == n:
            if self.check(word):
                global answer
                answer.append(word)
            return
        for char in parenthesis:
            self.dfs(idx+1, n, word+char, parenthesis)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        global answer
        answer = []
        parenthesis = ['(',')']
        self.dfs(0,n*2,'',parenthesis)
        return answer