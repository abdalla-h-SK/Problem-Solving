# 18
#   Time : O(n^3)
#   Space: O(1)

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        answers = []

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l, h = j+1, n-1

                while l < h:
                    summ = nums[i] + nums[j] + nums[l] + nums[h]
                    if summ == target:
                        answers.append([nums[i], nums[j], nums[l], nums[h]])
                        l += 1
                        h -= 1
                        while l < h and nums[l] == nums[l-1]:
                            l += 1
                        while l < h and nums[h] == nums[h+1]:
                            h -=1
                    elif summ > target:
                        h -= 1
                    else:
                        l += 1

        return answers