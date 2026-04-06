# 56

# my solution ->

#   time : O(n log(n))
#   space: O(n)

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged