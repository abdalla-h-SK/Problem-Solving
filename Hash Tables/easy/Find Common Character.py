# 1002
# my solution ->

from collections import Counter
class Solution(object):
    def commonChars(self, words):
        n = len(words)
        for i in range(n):
            words[i] = Counter(words[i])
        
        ans = []
        for k in words[0]:
            min_freq = float('inf')
            for counter in words:
                min_freq = min(min_freq, counter[k])
            
            ans.extend([k] * min_freq)
        
        return ans