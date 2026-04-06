# 347
# my solution ->

# Time : O(n log(k))
# Space: O(n + k)

import heapq, collections
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        heap = []
        for num, c in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, num))
            else:
                heapq.heappushpop(heap, (c, num))
        
        return list(map(lambda x:x[1] , heap))
    
    
# another solution ->

class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        n = len(nums)
        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []

        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret
    
    # Time : O(n)
    # Space: O(n)