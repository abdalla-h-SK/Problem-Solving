# 680
# my solution ->

class Solution(object):
    def validPalindrome(self, s):
        n = len(s)
        
        def palindrome(l, r, lives):
            if l >= r:
                return True

            if s[l] == s[r]:
                return palindrome(l+1, r-1, lives)
            else:
                if lives:
                    return palindrome(l+1, r, False) or palindrome(l, r-1, False)
                else:
                    return False
            
        return palindrome(0, n-1, True)