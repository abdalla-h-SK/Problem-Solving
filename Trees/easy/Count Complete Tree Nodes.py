# 222
# O(log(n) ^2)

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        l, r = 0, 0
        left = right = root
        
        while left:
            l += 1
            left = left.left
        while right:
            r += 1
            right = right.right
        
        if l == r:
            return 2 ** l - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)