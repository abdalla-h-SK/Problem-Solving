# 290
# my solution ->

from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
            return False
            
        patterns = defaultdict(str)
        for i, ltr in enumerate(pattern):
            if patterns[ltr] and patterns[ltr] != s[i]:
                return False
            patterns[ltr] = s[i]
        return True