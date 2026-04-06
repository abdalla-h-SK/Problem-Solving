# 1796
# my solution ->

from collections import heapq

class Solution(object):
    def secondHighest(self, s):
        nums = set()
        heap = []

        for i in s:
            if i.isdigit() and int(i) not in nums:
                nums.add(int(i))
                heapq.heappush(heap, int(i))
        
        for i in range(len(heap) - 2):
            heapq.heappop(heap)
        
        return heap[0] if len(heap) >= 2 else -1