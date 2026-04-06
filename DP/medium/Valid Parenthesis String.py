# 678
# my solution -> It didn't work with large inputs due to TLE

class Solution(object):
    def checkValidString(self, s):
        n = len(s)
        self.ans = False

        def validate(i, stk):
            if i == n:
                if not stk:
                    self.ans = True
                return 

            if s[i] == '(':
                stk.append(i)
                validate(i+1, stk)
                if stk and stk[-1] == i:
                    stk.pop()

            elif s[i] == ')':
                if not stk:
                    return
                temp = stk.pop()
                validate(i+1, stk)
                stk.append(temp)
            
            elif s[i] == '*':
                stk.append(i)
                validate(i+1, stk)
                if stk and stk[-1] == i:
                    stk.pop()
                
                if stk:
                    temp = stk.pop()
                    validate(i+1, stk)
                    stk.append(temp)
                
                validate (i+1, stk)
        
        stack = []
        validate(0, stack)

        return self.ans
    
    
# another solution -> The balance trick is good and better than using stack and it also backtrack it self rather than popping

class Solution(object):
    def checkValidString(self, s):
        n = len(s)
        memo = {}

        def dp(i, balance):
            if (i, balance) in memo:
                return memo[(i, balance)]

            if i == n:
                return balance == 0

            result = False

            if s[i] == '(':
                result = dp(i + 1, balance + 1)

            elif s[i] == ')':
                if balance > 0:
                    result = dp(i + 1, balance - 1)
                else:
                    result = False

            elif s[i] == '*':
                result = (
                    dp(i + 1, balance + 1)
                    or (balance > 0 and dp(i + 1, balance - 1))
                    or dp(i + 1, balance)
                )

            memo[(i, balance)] = result
            return result

        return dp(0, 0)