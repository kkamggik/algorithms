class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cnt = 1
        prev = str(chars[0])
        n = len(chars)
        idx = 0
        for i in range(1,n):
            c = str(chars[i])
            if c==prev:
                cnt += 1 
            else:
                chars[idx] = prev
                idx += 1
                if cnt > 1:
                    cnt = str(cnt)
                    for i in range(len(cnt)):
                        chars[idx] = cnt[i]
                        idx += 1
                prev = c
                cnt = 1
        if cnt >= 1:
            chars[idx] = prev
            idx += 1
            if cnt > 1:
                cnt = str(cnt)
                for i in range(len(cnt)):
                    chars[idx] = cnt[i]
                    idx += 1
        return idx