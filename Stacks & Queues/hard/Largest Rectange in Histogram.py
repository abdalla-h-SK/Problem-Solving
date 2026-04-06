# 84 
# my solution -> after explaining tho!
class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        max_area = 0

        for i in range(n):
            index = i
            while stack and heights[i] < stack[-1][0]:
                h, idx = stack.pop()
                area = (i - idx) * h
                max_area = max(max_area, area)
                index = idx
            stack.append((heights[i], index))
        
        while stack:
            h, idx = stack.pop()
            area = (n - idx) * h
            max_area = max(max_area, area)
        
        return max_area
        # Time: O(n)
        # Space: O(n)

