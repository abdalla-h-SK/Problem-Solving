# 647
# my solution ->

class Solution(object):
    def countSubstrings(self, s):
        def expandAroundCenter(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
            return res

        ans  = 0

        for i in range(len(s)):
            ans += expandAroundCenter(i, i)
            ans += expandAroundCenter(i, i + 1)

        return ans