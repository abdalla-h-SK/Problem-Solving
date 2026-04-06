# 2405
# my solution ->

class Solution(object):
    def partitionString(self, s):
        ltrs = set()
        ans = 0

        for i in s:
            if i not in ltrs:
                ltrs.add(i)
            else:
                ans += 1
                ltrs = {i}
        
        return ans + 1