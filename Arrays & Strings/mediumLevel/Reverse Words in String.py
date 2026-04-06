# 151

# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def reverseWords(self, s):

        return " ".join(s.split()[::-1])
    
