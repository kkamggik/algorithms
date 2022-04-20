class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        position = dict()
        for idx,val in enumerate(arr):
            position[val] = idx
        for piece in pieces:
            if piece[0] not in position: return False
            pos = position[piece[0]]
            for i in range(1,len(piece)):
                pos += 1
                if piece[i] not in position: return False
                if position[piece[i]]!=pos: return False
        return True
                    