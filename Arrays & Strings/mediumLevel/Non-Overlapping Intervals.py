# 435
# my solution -> Chat Gpt Hint !!

#   Time : O(n log(n)) , Space : O(n)

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda interval: interval[1])
        grap, ans = None, 0

        for interval in intervals:
            if not grap or grap[1] <= interval[0]:
                grap = interval
            else:
                ans += 1
        
        return ans