class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0]*26
        stack = []
        flag = [False]*26
        for c in s:
            cnt[ord(c)-ord('a')] += 1
        for c in s:
            cnt[ord(c)-ord('a')] -= 1
            if stack and stack[-1] > c and flag[ord(c)-ord('a')]==False:
                while stack and stack[-1] > c:
                    if cnt[ord(stack[-1])-ord('a')] > 0:
                        x = stack.pop()
                        flag[ord(x)-ord('a')] = False
                    else: break
                flag[ord(c)-ord('a')] = True
                stack.append(c)           
            elif flag[ord(c)-ord('a')]==True: continue
            else:
                flag[ord(c)-ord('a')] = True
                stack.append(c)
        return ''.join(stack)            