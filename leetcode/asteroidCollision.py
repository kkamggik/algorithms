class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            if a < 0:
                while stack and 0<stack[-1]<abs(a):
                    stack.pop()
                if stack and stack[-1]==abs(a):
                    stack.pop()
                elif stack and stack[-1]>abs(a):
                    continue
                else:
                    stack.append(a)
            else:
                stack.append(a)
        return stack