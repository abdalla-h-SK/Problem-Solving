# 575
# my solution ->

class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        kinds = set(candyType)

        return min(len(kinds), n // 2)