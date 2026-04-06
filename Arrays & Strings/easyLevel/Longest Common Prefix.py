# 14

# my solution ->

#   time : O(n * m)
#   space: O(1)

class Solution:
    def longestCommonPrefix(self, strs):
        min_length = len(min(strs, key=len))
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return strs[0][:i]