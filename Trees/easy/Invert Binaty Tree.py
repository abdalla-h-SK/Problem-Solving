# 226

# my solution ->

#   Time : O (n)
#   Space: O (h)      Height of the Tree

class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        def invert(root):
            curr = root
            if not curr:
                return
            
            curr.left, curr.right = curr.right, curr.left
            invert(curr.left)
            invert(curr.right)
            
        invert(root)
        
        return root
