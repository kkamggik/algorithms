class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        answer = 0
        for d in digits:
            answer *= 10
            answer += int(d)
        rst = str(answer+1)
        answer = []
        for r in rst:
            answer.append(int(r))
        return answer