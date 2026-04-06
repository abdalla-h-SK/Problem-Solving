# 1584

    # Time : O(n^2 * log(n))
    # Space: O(n^2)

import heapq
class Solution(object):
    def minCostConnectPoints(self, points):

        n = len(points)
        seen = set()
        heap = [(0, 0)]
        total_dist = 0

        while len(seen) < n:
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            total_dist += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    min_dist = abs(xj - xi) + abs(yj - yi)
                    heapq.heappush(heap, (min_dist, j))
        
        return total_dist