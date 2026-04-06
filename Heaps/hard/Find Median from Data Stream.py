# 295

import heapq
class MedianFinder(object):

    def __init__(self):
        self.small, self.big = [], []

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.big and -self.small[0] > self.big[0]:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        

        if len(self.small) - 1 > len(self.big):
            heapq.heappush(self.big, -heapq.heappop(self.small))
        
        if len(self.big) - 1 > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self):
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return float(self.big[0] - self.small[0]) / 2