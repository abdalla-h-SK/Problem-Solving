# 77
# my solution ->

class Solution(object):
    def combine(self, n, k):
        res, sol = [], []

        def backtrack():
            if len(sol) == k:
                res.append(sol[:])
                return
            
            for i in range(1, n+1):
                if not sol or i > sol[-1]:
                    sol.append(i)
                    backtrack()
                    sol.pop()

        backtrack()
        return res
    

# another solution -> This is wide better!

class Solution(object):
    def combine(self, n, k):
        res, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return 
            
            left = x
            still_need = k-len(sol)

            if left > still_need:
                backtrack(x-1)

            sol.append(x)
            backtrack(x-1)
            sol.pop()

        backtrack(n)
        return res