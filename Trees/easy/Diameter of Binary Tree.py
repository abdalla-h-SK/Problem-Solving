# 543
# my solution -> Be patient and trust the process 

#   Time : O (n)
#   Space: O (h)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        max_diameter = [0]
        
        def diameter(root):
            curr = root
            if not curr:
                return 0

            left = diameter(curr.left)
            right = diameter(curr.right)

            max_diameter[0] = max(max_diameter[0], left + right)

            return max(left, right) + 1

        diameter(root)
        return max_diameter[0]