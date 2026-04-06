# 22

# my soluiton -> I got some hints from chatgpt!

class Solution(object):
    def generateParenthesis(self, n):
        res, sol = [], []
        
        def backtrack(i, opens, closes):
            if i == n:
                res.append(''.join(sol[:]))
                return 

            if opens < n:
                sol.append("(")
                backtrack(i, opens+1, closes)
                sol.pop()

            if closes < opens:
                sol.append(")")
                backtrack(i+1, opens, closes+1)
                sol.pop()
            
        backtrack(0, 0, 0)
        return res