class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name) > len(typed): return False
        idx = i = 0
        while i < len(name):
            if idx >= len(typed): return False
            if name[i]==typed[idx]:
                i += 1
                idx += 1
            else:
                if i>0 and name[i-1]==typed[idx]:
                    idx += 1
                else: return False
            if i == len(name) and idx < len(typed):
                while idx < len(typed):
                    if name[-1] != typed[idx]: return False
                    idx += 1
        return True