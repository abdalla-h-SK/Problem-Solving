# 205
# my solution ->

from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):
        
        isoms = defaultdict(str)
        isoms_rev = defaultdict(str)

        for i, ltr in enumerate(s):
            if (isoms[ltr] and isoms[ltr] != t[i]) or (isoms_rev[t[i]] and isoms_rev[t[i]] != ltr):
                return False
            isoms[ltr] = t[i]
            isoms_rev[t[i]] = ltr

        return True