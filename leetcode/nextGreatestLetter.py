class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if letters[-1] <= target: return letters[0]
        start,end =  0, len(letters)-1
        while start <= end:
            mid = (start+end)//2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start]
                