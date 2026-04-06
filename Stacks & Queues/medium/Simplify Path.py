# 71
# my solution ->

class Solution(object):
    def simplifyPath(self, path):
        if path == '/':
            return '/'
        
        path = path.split('/')
        stack = []

        for i in path:
            if i == '.' or not i:
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return '/' + '/'.join(stack)