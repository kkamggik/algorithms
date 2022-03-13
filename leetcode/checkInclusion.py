class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False
        idx1, idx2 = 0,0
        arr1 = [0]*26
        arr2 = [0]*26
        for i in range(len(s1)):
            arr1[ord(s1[i])-97] += 1
            arr2[ord(s2[i])-97] += 1
        if arr1 == arr2: return True
        for i in range(len(s1), len(s2)):
            arr2[ord(s2[i])-97] += 1
            arr2[ord(s2[i-len(s1)])-97] -= 1
            if arr1 == arr2: return True
        return False