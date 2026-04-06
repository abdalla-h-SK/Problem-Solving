# 1448
# my solution ->

#   Time : O(n^2)
#   Space: O(n)

class Solution(object):
    def goodNodes(self, root):
        good = [0]
        stack = []

        def count(curr):
            if not curr:
                return
            
            if all(curr.val >= node_value for node_value in stack):
                good[0] += 1
            
            stack.append(curr.val)
            
            count(curr.left)
            count(curr.right)

            stack.pop()

        count(root)

        return good[0]
    
# a quite better solution ->

class Solution(object):
    def goodNodes(self, root):
        good_nodes = 0
        stk = [(root, float("-inf"))]

        while stk:
            node, largest = stk.pop()
            
            if largest <= node.val:
                good_nodes += 1

            largest = max(largest, node.val)
            
            if node.right: stk.append((node.right, largest))
            if node.left: stk.append((node.left, largest))

        return good_nodes

# Time Complexity: O(n)
# Space Complexity: O(n)