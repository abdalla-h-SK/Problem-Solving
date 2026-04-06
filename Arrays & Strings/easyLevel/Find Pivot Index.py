# 724
# my solution ->

#   Time : O(n) , Space : O(n)

class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        left_sum = right_sum = 0
        left_lst = [0] * n
        right_lst = [0] * n

        for i in range(n):
            j = -i-1
            left_lst[i] = left_sum
            right_lst[j] = right_sum
            left_sum += nums[i]
            right_sum += nums[j]

        for i in range(n):
            if left_lst[i] == right_lst[i]:
                return i
        return -1

# a better aproach !

class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        total = sum(nums)
        left_sum = 0

        for i in range(n):
            if left_sum == total-(left_sum + nums[i]):
                return i
            else:
                left_sum += nums[i]
        return -1