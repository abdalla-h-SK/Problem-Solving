# 455
# my solution ->

class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()

        if not (s and g):
            return 0

        j = 0
        content = 0
        for i in range(len(g)):
            while g[i] > s[j]:
                j += 1
                if j == len(s):
                    return content
            
            content += 1
            j += 1
            if j == len(s):
                return content
        
        return content