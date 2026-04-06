# 75

class Solution(object):
    def sortColors(self, nums):
        counts = [0, 0, 0]
        for color in nums:
            counts[color] += 1


        R, W, B = counts

        nums[:R] = [0] * R
        nums[R:R+W] = [1] * W
        nums[R+W:] = [2] * B

    # Time : O(n)
    # Space: O(1)