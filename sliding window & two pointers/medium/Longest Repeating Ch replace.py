# 424
# my solution ->

#   Time : O(n) 
#   Space: O(1) >> the alphabet has 26 letters 

from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        l = 0
        ans = 0
        counter = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1

            while (r - l + 1) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
                
            ans = max(ans, (r - l + 1))
        
        return ans
    
# another solution ->
class Solution:
    def characterReplacement(self, s , k):
        longest = 0
        l = 0
        counts = [0] * 26

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1

            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - 65] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest

# Time Complexity: O(n)
# Space Complexity: O(1)