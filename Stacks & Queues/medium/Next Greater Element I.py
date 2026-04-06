# 496
# my solution ->

# Time : O(n)
# Space: O(n)

from collections import defaultdict
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n_big = defaultdict(lambda: -1)
        n = len(nums2)
        stack = []

        for i in range(n):
            while stack and nums2[i] > nums2[stack[-1]]:
                idx = stack.pop()
                n_big[nums2[idx]] = nums2[i]
            stack.append(i)

        ans = []
        for num in nums1:
            ans.append(n_big[num])
        return ans