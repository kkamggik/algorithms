class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        direction = 1
        row = 0
        answer = [''] * numRows
        for c in s:
            answer[row] += c
            if direction == 1:
                row += 1
                if row == numRows:
                    direction = -1
                    row = numRows - 2
            else:
                row -= 1
                if row == -1:
                    direction = 1
                    row = 1
        return ''.join(answer)