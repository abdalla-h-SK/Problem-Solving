# 3
# my solution -> This is not the proper way of sliding window
from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ltrs = set()
        que = deque([])
        output = 0

        for i in range(len(s)):
            if s[i] in ltrs:

                output = max(len(que), output)

                while True:
                    delete = que.popleft()
                    ltrs.discard(delete)
                    if delete == s[i]:
                        break


            que.append(s[i])
            ltrs.add(s[i])
        
        return max(output, len(que))
    

# another solution ->
class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest

# Time Complexity: O(n)
# Space Complexity: O(n) (but because we're limited to common characters only, it's actually O(1))