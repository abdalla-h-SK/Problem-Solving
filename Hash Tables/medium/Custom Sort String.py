# 791
# my solution ->

class Solution(object):
    def customSortString(self, order, s):
        que = {}

        for i in s:
            que[i] = que.get(i, 0) + 1

        res = ''
        for i in order:
            if i in que:
                res += i * que[i]
                del que[i]
        
        for i in que:
            res += i * que[i]
        
        return res