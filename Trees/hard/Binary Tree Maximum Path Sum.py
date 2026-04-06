# 124
# my solution ->        I'm Inevitable

#   Time : O(n) , Space : O(h)

class Solution(object):
    def maxPathSum(self, root):
        max_sum = [float('-inf')]
        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left < 0:
                left = 0
            if right < 0:
                right = 0

            max_sum[0] = max(max_sum[0], (left + right + curr.val))

            return max(left, right) + curr.val
        
        dfs(root)
        return max_sum[0]