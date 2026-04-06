# 646
# my solution ->

class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key= lambda interval:interval[1])
        grap, ans = None, len(pairs)

        for pair in pairs:
            if not grap or grap[1] < pair[0]:
                grap = pair
            else:
                ans -= 1          # so if there are alot of overlaps we will take only one interval in this conditoin...
        
        return ans