# 128 
# my solution ->

# Time : O(n)
# Space: O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        
        longest = 0
        s = set(nums)
        
        for num in nums:
            if num-1 not in s:
                length = 1
                while num + 1 in s:
                    length += 1
                    num += 1
                longest = max(longest, length)
        return longest