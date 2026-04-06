# 17
# my soluiton ->

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        res, sol = [], []
        n = len(digits)
        phone_number_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def backtrack(i):
            if len(sol) == n:
                res.append(''.join(sol[:]))
                return

            num = digits[i]
            for letter in phone_number_mapping[num]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
                
        backtrack(0)
        return res