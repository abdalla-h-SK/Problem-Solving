# 39

# my solution ->

class Solution(object):
    def combinationSum(self, candidates, target):
        res, sol = [], []
        n = len(candidates)

        def backtrack(sum_sol):

            if sum_sol == target:
                res.append(sol[:])
                return

            elif sum_sol > target:
                return
            
            for i in candidates:
                if not sol or i >= sol[-1]:
                    sol.append(i)
                    backtrack(sum_sol + i)
                    sol.pop()

        backtrack(0)
        return res
    

# another solution ->

class Solution(object):
    def combinationSum(self, candidates, target):
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            elif curr_sum > target or i == n:
                return
            
            backtrack(i+1, curr_sum)

            sol.append(candidates[i])
            backtrack(i, curr_sum + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return res