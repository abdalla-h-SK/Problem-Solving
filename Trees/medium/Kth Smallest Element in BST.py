# 230

# my solution -> It's a BTS so we can avoid sorting

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def kthSmallest(self, root, k):
        nodes = []

        def smallest(curr):
            if not curr:
                return 
            
            smallest(curr.left)
            nodes.append(curr.val)
            smallest(curr.right)
        
        smallest(root)
        
        i = 0
        for j in range(k - 1):
            i += 1
        
        return nodes[i]
    
# a Better solution ->

class Solution(object):
    def kthSmallest(self, root, k):
        count = [k]
        ans = [0]

        def smallest(curr):
            if not curr:
                return 
            
            smallest(curr.left)
            if count[0] == 1:
                ans[0] = curr.val
            count[0] -= 1
            if count[0] > 0:
                smallest(curr.right)
        
        smallest(root)

        return ans[0]