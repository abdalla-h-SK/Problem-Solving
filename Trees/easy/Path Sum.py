# 112
# my solution ->

#   Time : O(n)
#   Space: O(n)

class Solution(object):
    def hasPathSum(self, root, targetSum):
        flag = [False]
        summ = [0]

        def path(curr):
            if not curr:
                return
            
            summ[0] += curr.val
            if summ[0] == targetSum and not(curr.right or curr.left):
                flag[0] = True
                return
            
            path(curr.left)
            if flag[0]:
                return
            path(curr.right)

            summ[0] -= curr.val
        
        path(root)
    
        return flag[0]
    
# another solution ->

class Solution(object):
    def hasPathSum(self, root, targetSum):

        def has_sum(root, cur_sum):
            if not root:
                return False

            cur_sum += root.val

            if not root.left and not root.right:
                return cur_sum == targetSum
            
            return has_sum(root.left, cur_sum) or \
                   has_sum(root.right, cur_sum)
        
        return has_sum(root, 0)
        # Time: O(n)
        # Space: O(h) or O(n)