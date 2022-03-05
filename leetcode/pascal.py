class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        answer = [[1]]
        for i in range(1,numRows):
            rst = []
            rst.append(1)
            for j in range(1,len(answer[i-1])):
                rst.append(answer[i-1][j-1]+answer[i-1][j])
            rst.append(1)
            answer.append(rst)
        return answer
            