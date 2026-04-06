# 937
# my solution ->

# Time : O(n log(k))
# Space: O(k)

import heapq, math
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for i in range(len(points)):
            if len(heap) < k:
                heapq.heappush(heap, (-( (points[i][0])**2 + (points[i][1])**2 ), points[i]))
            else:
                heapq.heappushpop(heap, (-( (points[i][0])**2 + (points[i][1])**2 ), points[i]))

        return list(map(lambda x:x[1], heap))