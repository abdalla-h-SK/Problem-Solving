# 104
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def maxDepth(self, root):
        hs = [0, 0]
        
        def height(root):
            curr = root
            if not curr:
                return
            
            hs[0] += 1
            hs[1] = max(hs[0], hs[1])

            height(curr.left)
            height(curr.right)

            hs[0] -= 1

        height(root)

        return hs[1]
    
# another solution ->

class Solution(object):
    def maxDepth(self, root):
        
        if not root:
            return 0
        
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        
        return max(left_depth, right_depth) + 1
    
    # Time : O(n)
    # Space: O(n)