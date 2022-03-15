class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        paths = path.split('/')
        for path in paths:
            path = str(path)
            if not path: continue
            if path=='..':
                if stack: stack.pop()
            elif path=='.': continue
            else: stack.append(path)
        if not stack: return '/'
        return '/'+'/'.join(stack)