# 1614
# my solution ->

class Solution(object):
    def maxDepth(self, s):
        pare = 0
        ans = 0

        for i in s:
            if i == '(':
                pare += 1
                ans = max(ans, pare)

            elif i == ')':
                pare -= 1
        
        return ans