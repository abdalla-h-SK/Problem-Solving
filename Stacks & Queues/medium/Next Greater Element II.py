# 503
# my solution ->

class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                ans[idx] = nums[i]
            stack.append(i)

        l, r = 0, len(stack) - 1

        while l < n and r > -1:
            if nums[l] > nums[stack[r]]:
                ans[stack[r]] = nums[l]
                r -= 1
            else:
                l += 1
        
        return ans

        # for i in range(n):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         idx = stack.pop()
        #         ans[idx] = nums[i]
        # return ans