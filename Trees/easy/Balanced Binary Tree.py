# 110

class Solution(object):
    def isBalanced(self, root):
        balanced = [True]

        def height(root):
            if not root:
                return 0

            if balanced[0] is False:
                return 0

            left = height(root.left)
            right = height(root.right) 

            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left, right)

        height(root)
        return balanced[0]
    
    # Time : O (n)
    # Space: O (h)