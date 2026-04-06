# 152

class Solution(object):
    def maxProduct(self, nums):
        prefix,suffix,max_so_far = 0, 0 , float('-inf')
        for i in range(len(nums)):
            prefix = (prefix or 1) * nums[i]
            suffix = (suffix or 1) * nums[-i-1]
            max_so_far = max(max_so_far, prefix,suffix)
        return max_so_far

# another solution ->

class Solution(object):
    def maxProduct(self, nums):
        res = max(nums)

        min_cur, max_cur = 1, 1

        for n in nums:
            if n == 0:
                min_cur, max_cur = 1, 1
                continue
            
            temp = max_cur * n
            max_cur = max(temp, n * min_cur, n)
            min_cur = min(temp, n * min_cur, n)
            res = max(res, max_cur)
        
        return res