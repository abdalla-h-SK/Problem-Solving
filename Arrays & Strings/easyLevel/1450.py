# my soluiton ->
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        n = len(startTime)
        ans = 0
        for i in range(n):
            if startTime[i] > queryTime:
                continue
            if endTime[i] < queryTime:
                continue

            ans += 1
        
        return ans