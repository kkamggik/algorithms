class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        answer = []
        dic = {}
        for s in strs:
            string = str(''.join(sorted(s)))
            if string not in dic:
                dic[string] = [s]
            else:
                dic[string].append(s)
        for key in dic.keys():
            rst = []
            for k in dic[key]:
                rst.append(k)
            answer.append(rst)
        return answer