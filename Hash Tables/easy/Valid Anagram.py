# 242
# my solution ->

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        counter = Counter(t)

        for ltr in s:
            if ltr not in counter:
                return False
            
            elif counter[ltr] > 1:
                counter[ltr] -= 1
                
            elif counter[ltr] == 1:
                del counter[ltr]
        
        if counter:
            return False
        return True