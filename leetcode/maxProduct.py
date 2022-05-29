class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dic = defaultdict(int)
        ans = 0
        for word in words:
            mask = 0
            for c in word:
                # char의 위치를 bit로 저장함니다..
                mask |= (1 << (ord(c) - 97))
            dic[word] = mask
        for w1, w2 in combinations(dic.keys(), 2):
            # 만약 두 word가 겹치는게업다면...!
            if dic[w1] & dic[w2] == 0: 
                ans = max(ans, len(w1)*len(w2))
        return ans
                