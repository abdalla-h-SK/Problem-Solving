# 1137
# my soluiton ->

class Solution(object):
    def tribonacci(self, n):
        memo = {0:0, 1:1, 2:1}

        def tribo(i):
            if i in memo:
                return memo[i]
            
            memo[i] = tribo(i-1) + tribo(i-2) + tribo(i-3)
            return memo[i]
        
        return tribo(n)