# 98
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def isValidBST(self, root):
        valid = [True]
        prev = [None]

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            if valid[0] == False:
                return
            if prev[0] is not None and node.val <= prev[0]:  
                valid[0] = False
            prev[0] = node.val

            dfs(node.right)

        dfs(root)
        return valid[0]
    
# another solution ->

class Solution(object):
    def isValidBST(self, root):
        def is_valid(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_valid(node.left, minn, node.val) and is_valid(node.right, node.val, maxx)

        return is_valid(root, float('-inf'), float('inf'))
    
    #   Space: O(h)