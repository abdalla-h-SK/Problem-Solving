# 530
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def getMinimumDifference(self, root):
        smallest = []
        def smallest_two(curr):
            if not curr:
                return
            
            smallest_two(curr.left)
            smallest.append(curr.val)
            smallest_two(curr.right)
        
        smallest_two(root)

        minn = float('inf')
        for i in range(len(smallest) - 1):
            minn = min(minn, smallest[i+1] - smallest[i])
        
        return minn
    
# a Better solution ->

class Solution(object):
    def getMinimumDifference(self, root):
        min_diff = [float('inf')]
        prev = [None]

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if prev[0] is not None:
                min_diff[0] = min(min_diff[0], node.val - prev[0])
            prev[0] = node.val

            dfs(node.right)

        dfs(root)
        return min_diff[0]