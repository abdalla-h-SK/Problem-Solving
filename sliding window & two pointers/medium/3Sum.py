# 15
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        answers = []

        for i in range(n):
            l = i+1
            h = n-1

            if nums[i] > 0:
                break

            elif i > 0 and nums[i] == nums[i-1]:
                continue

            while l < h:
                summ = nums[i] + nums[l] + nums[h]
                if summ == 0:
                    answers.append([nums[i], nums[l], nums[h]])
                    l, h = l+1, h-1
                    while l < h and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and nums[h] == nums[h+1]:
                        h -=1
                elif summ > 0:
                    h -= 1
                else:
                    l += 1

        return answers
    
#   Time : O(n^2)
#   Space: (1)