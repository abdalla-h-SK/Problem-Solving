# 300

class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

# I'v tried for this one in vain!

# Here is a great soluiton ->
from bisect import bisect_left # -> returns the place where the number should be inserted in the list as it accepts (list , num)
class Solution(object):
    def lengthOfLIS(self, nums):

        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)