# 1046
# my solution ->

#   Time : O(n log(n))
#   Space: O(1)

import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
               
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, x-y)

        return -stones[0] if stones else 0