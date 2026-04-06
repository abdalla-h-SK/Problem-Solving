# 91
# almost figured it out!

class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        memo = {}  

        def codes(i):
            if i in memo:
                return memo[i]

            if i == n:
                return 1

            if s[i] == '0':
                return 0

            result = codes(i + 1)

            if i + 1 < n and '10' <= s[i:i+2] <= '26': 
                result += codes(i + 2)

            memo[i] = result
            return result

        return codes(0)