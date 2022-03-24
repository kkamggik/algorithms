class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = str(n)
        answer = ''
        cnt = 0
        for c in num[::-1]:
            answer += c
            cnt += 1
            if cnt == 3:
                answer += '.'
                cnt = 0
        if answer[-1] == '.': answer = answer[:-1]
        return answer[::-1]