# 452
# my solution ->

#   Time : O(n log(n))
#   Space: O(n)

class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda point:point[0])
        ans = []

        for point in points:
            if not ans or point[0] > ans[-1][1]:
                ans.append(point)
            else:
                ans[-1] = [point[0], min(ans[-1][1], point[1])]
        
        return len(ans)