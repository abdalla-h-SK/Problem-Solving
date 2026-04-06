# 76
# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import defaultdict, Counter

class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""
        
        if t in s:
            return t
        
        counter, window = Counter(t), defaultdict(int)
        have, need = 0, len(counter)

        ans = [float('inf'), 0, len(s) - 1]
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if counter[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r + 1
                
                c = s[l]
                window[c] -= 1
                if window[c] < counter[c]:
                    have -= 1
                l += 1
            
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]