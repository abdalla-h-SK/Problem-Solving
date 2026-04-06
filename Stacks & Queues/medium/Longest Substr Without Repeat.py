# 3

# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import deque

def get_max_len(s):

    ltrs = set()
    que = deque([])
    output = 0

    for i in range(len(s)):
        if s[i] in ltrs:

            if len(que) > output:
                output = len(que)

            while True:
                delete = que.popleft()
                ltrs.discard(delete)
                if delete == s[i]:
                    break


        que.append(s[i])
        ltrs.add(s[i])
    
    if len(que) > output:
        output = len(que)
    return output


# another solution using sliding window ->

#   Time : O(n)
#   Space: O(1)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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