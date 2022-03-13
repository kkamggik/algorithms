class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        right = {c:i for i,c in enumerate(s)}
        answer = []
        start,end = 0,0
        for i,c in enumerate(s):
            end = max(end, right[c])
            if end == i:
                answer.append(end-start+1)
                start = end+1
        return answer
        