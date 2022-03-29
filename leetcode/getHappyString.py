class Solution(object):
    def find(self, idx, s, n, k):
        if len(s) == n:
            global answer, cnt
            cnt += 1
            if cnt == k: answer = s
            return
        for i in range(3):
            if idx == i: continue
            self.find(i, s+chr(97+i), n, k)
                
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        global answer, cnt
        cnt = 0
        answer = ''
        self.find(-1,'',n, k)
        return answer
        