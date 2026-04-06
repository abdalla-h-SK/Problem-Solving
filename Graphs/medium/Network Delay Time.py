# 743
# my solution ->

    # Time : O(n^2 * log(n))
    # Space: O(n^2)

import heapq
from collections import defaultdict
class Solution(object):
    def networkDelayTime(self, times, n, k):

        seen = set()
        heap = [(0, k)]
        time = 0

        gragh = defaultdict(list)
        for x, y, t in times:
            gragh[x].append((t, y))

        while heap:
            while heap and heap[0][0] == time:
                t_, signal =  heapq.heappop(heap)
                if signal in seen:
                    continue
                seen.add(signal)
                for t_ar, sig in gragh[signal]:
                    if sig not in seen:
                        heapq.heappush(heap, (t_ar + time, sig))

            if len(seen) == n:
                break
            time += 1

        return time if len(seen) == n else -1