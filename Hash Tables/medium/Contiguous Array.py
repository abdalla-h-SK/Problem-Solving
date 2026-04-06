# 525

# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def findMaxLength(self, nums):
        seen = {}
        seen[0] = -1
        count = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in seen:
                max_length = max(max_length, i-seen[count])
            else:
                seen[count] = i

        return max_length