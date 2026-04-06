# my solution ->

class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        op = 0

        for i in range(k):
            if blocks[i] == 'W':
                op += 1

        ans = op
        for i in range(k, n):
            if blocks[i] == 'W':
                op += 1
            if blocks[i - k] == 'W':
                op -= 1
            
            ans = min(ans, op)
        
        return ans