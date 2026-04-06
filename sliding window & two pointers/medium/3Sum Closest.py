# 16
# my sloution ->

#   Time : O(n^2)
#   Space: O(1)

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        min_diff = float('inf')

        for i in range(n - 2):
            l = i+1
            h = n-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < h:
                summ = nums[i] + nums[l] + nums[h]
                if summ == target:
                    return summ
                elif summ > target:
                    h -= 1
                    if summ-target < min_diff:
                        min_diff = summ-target
                        closest = summ
                else:
                    l += 1
                    if target-summ < min_diff:
                        min_diff = target-summ
                        closest = summ

        return closest  