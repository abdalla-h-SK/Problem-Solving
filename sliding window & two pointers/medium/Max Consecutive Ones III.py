# 1004
# my solution ->

#   Time : O(n)
#   Space: O(n)

from collections import deque

class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        zeros = deque([])

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros.append(r)

            if len(zeros) > k:
                l += 1
            
            if zeros and l > zeros[0]:
                zeros.popleft()
            
        return( r - l + 1 )

# another solution ( I got one like this tho!) ->
class Solution:
    def longestOnes(self, nums, k):
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            w = r - l + 1
            max_w = max(max_w, w)

        return max_w

# Time Complexity: O(n)
# Space Complexity: O(1)
    
