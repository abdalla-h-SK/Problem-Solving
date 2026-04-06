# 11
# my solution ->

#   Time : O(n)
#   Space: O(1)

class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        max_area = float('-inf')

        while i < j:
            c = min(height[i], height[j])
            area = c * (j-i)
            max_area = max(area, max_area)

            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        
        return max_area